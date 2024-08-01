import config
import sys
import re
import datetime
import os
import time

from auth.token import Token
from services.quotes_service.quotes_servise import MarketDataService
from services.instruments_servise.instruments_servise import InstrumentsService
from services.operations_service.operations_service import Operations
from services.accounts_service.accounts_service import Accounts
from db_integration import DBIntegration
from sql_lib.script_normalizer import ScriptNormalizer
from pprint import pprint
import shelve
from pathlib import Path
#from multipledispatch import dispatch

import my_logger
log = my_logger.setup_applevel_logger(file_name = 'data_updater.log')

class DataUpdater(object):
    def __init__(self):
        path = config.get_config()["temp_file"]
        self.temp_file = os.path.abspath(os.path.join(*path))
        if not os.path.exists(self.temp_file):
            os.makedirs(self.temp_file)
        self.token=self.set_token()

    def set_token(self):
        token = Token()
        return token.access_token

    def test(self):
        print('test')

    def update_accounts_in_local_db(self):
        '''Обновляет список счетов в локальной БД
        '''
        log.debug(f'{__name__} -> RUN update_accounts_in_local_db()')
        sql_query=ScriptNormalizer("accounts").select()
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)

        accounts_id_list=[]
        for item in data:
            accounts_id_list.append(str(item[0]))

        request=Accounts(TOKEN=self.token)
        response_data=request.get_my_accounts()

        for item in response_data:
            if item["account_id"] not in accounts_id_list:
                sql_query=ScriptNormalizer("accounts", new_data=item).insert()
                #Создание подключения к БД
                db_connection=DBIntegration()
                DBIntegration.script_executer_with_commit(db_connection,sql_query)

    def update_positions_in_temp_file(self):
        '''Метод обновляет временный файл
        актуальными данными по позициям на всех счетах брокера
        '''
        log.debug(f'{__name__} -> RUN update_positions_in_temp_file()')
        sql_query=ScriptNormalizer("accounts").select()
        #logging.info(f'{__name__} -> update_positions_in_temp_file() -> sql_query: {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        account_id_list=[]
        for i in range(len(data)):
            account_id_list.append(str(data[i][0]))

        #Получим новые данные от сервера
        body={"account_id_list":account_id_list}
        response_data=Operations(TOKEN=self.token,BODY=body)
        response_data_list=response_data.get_my_positions_by_account()

        curent_time=datetime.datetime.now()
        positions={"last_update":curent_time,
                   "positions_info":response_data_list}

        #если временная директория не существует, необходимо ее создать

        temp_dir=Path(os.path.dirname(self.temp_file))
        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)
        #Сохраним новые данные во временный файл
        #Откроем временный файл
        shelveFile=shelve.open(self.temp_file)
        shelveFile['positions_info']=positions
        shelveFile.close()

    def get_local_db_instruments(self):
        """Возвращает список инструментов сохраненных в локальной БД
        """
        #Столбцы выборки
        cols_list=["figi"]
        #Создаем запрос к БД
        sql_query=ScriptNormalizer("instruments").select(cols_list=cols_list)
        log.debug(f'{__name__} -> get_local_db_instruments() -> sql_query: {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        #logging.info(f'{__name__} -> get_local_db_instruments data: {data}')
        return data

    def update_temp_file_with_curriencies(self):
        '''Метод Обновляет котировки валюты в локальном файле
        для прикладных нужд по следующему списку:
        "BBG0013HGFT4" - USD/RUB
        '''
        log.debug(f'{__name__} -> RUN update_temp_file_with_curriencies()')
        request=MarketDataService(TOKEN=self.token)
        request.update_local_currencies()

    def update_db_with_new_instruments_list(self):
        """Обновляет БД инструментов доступных для торговли
        """
        #Получим список инструментов в локальной БД
        db_data=self.get_local_db_instruments()
        figi_list=[]
        for item in db_data:
            figi_list.append(item[0])

        #Получим актуальный список акций доступных на рынке
        request=InstrumentsService(TOKEN=self.token)
        shares_list=request.get_shares_list()
        #Обновим БД если окажется что инструмента нет в локальной БД
        for instrument in shares_list:
            if instrument.figi not in figi_list:
                #logging.info(f'{__name__} -> update_db_with_instruments_list()-> instrument.figi: {instrument}')
                instrument_json={"currency":instrument.currency,
                                 "figi":instrument.figi,
                                 "isin":instrument.isin,
                                 "lot":instrument.lot,
                                 "min_price_increment":instrument.lot,
                                 "ticker_name":instrument.name,
                                 "ticker":instrument.ticker,
                                 "instrument_type":"Stock"
                                }
                sql_query=ScriptNormalizer("instruments", new_data=instrument_json).insert()
                #Создание подключения к БД
                db_connection=DBIntegration()
                DBIntegration.script_executer_with_commit(db_connection,sql_query)
        #Получим актуальный список облигаций доступных на рынке
        bond_list=request.get_bonds_list()
        #Обновим БД если окажется что инструмента нет в локальной БД
        for instrument in bond_list:
            if instrument.figi not in figi_list:
                #logging.info(f'{__name__} -> update_db_with_instruments_list() -> instrument.figi: {instrument}')
                #pprint(instrument)
                instrument_json={"currency":instrument.currency,
                                 "figi":instrument.figi,
                                 "isin":instrument.isin,
                                 "lot":instrument.lot,
                                 "min_price_increment":instrument.lot,
                                 "ticker_name":instrument.name,
                                 "ticker":instrument.ticker,
                                 "instrument_type":"Bond"
                                }
                sql_query=ScriptNormalizer("instruments", new_data=instrument_json).insert()
                #Создание подключения к БД
                db_connection=DBIntegration()
                DBIntegration.script_executer_with_commit(db_connection,sql_query)

        #Получим актуальный список фондов доступных на рынке
        etf_list=request.get_etf_list()
        #Обновим БД если окажется что инструмента нет в локальной БД
        for instrument in etf_list:
            if instrument.figi not in figi_list:
                #logging.info(f'{__name__} -> update_db_with_instruments_list() -> instrument.figi: {instrument}')
                instrument_json={"currency":instrument.currency,
                                 "figi":instrument.figi,
                                 "isin":instrument.isin,
                                 "lot":instrument.lot,
                                 "min_price_increment":instrument.lot,
                                 "ticker_name":instrument.name,
                                 "ticker":instrument.ticker,
                                 "instrument_type":"Etf"
                                }
                sql_query=ScriptNormalizer("instruments", new_data=instrument_json).insert()
                #Создание подключения к БД
                db_connection=DBIntegration()
                DBIntegration.script_executer_with_commit(db_connection,sql_query)

if __name__ == '__main__':

    data_updater=DataUpdater()

    while True:
        try:
            data_updater.update_positions_in_temp_file()
            data_updater.update_temp_file_with_curriencies()
            data_updater.update_accounts_in_local_db()
            data_updater.update_db_with_new_instruments_list()
            time.sleep(config.get_config()["update_timer"])
        except KeyboardInterrupt:    #Без этой строчки код будет выполняться бесконечно при любом количестве ошибок
            log.debug(f' Завершение работы: KeyboardInterrupt')
            is_running=False
            sys.exit(0)
        except Exception as e:
            log.error(f'ERROR: {e}', exc_info=True)
            time.sleep(3)    #Перезапуск процесса скрипта спустя n сек
