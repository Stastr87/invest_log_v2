import sys, datetime, os, time, platform, shelve

from auth.token import Token
from services.quotes_service.quotes_servise import MarketDataService
from services.instruments_service.instruments_service import InstrumentsService
from services.operations_service.operations_service import Operations
from services.accounts_service.accounts_service import Accounts
from db_integration import DBIntegration
from sql_lib.script_normalizer import ScriptNormalizer
from pprint import pprint
from pathlib import Path

import config
logger_config = config.get_logger_config()

if 'wind' in str(platform.system()).lower():
    data_updater_log_path = logger_config['path']
else:
    data_updater_log_path = logger_config['alternative_path']

data_updater_log_file = logger_config['data_updater']['name']
file_mode = logger_config['data_updater']['mode']
logger_level = logger_config['data_updater']['level']

import logging
# Настройка логирования
log_data_updater = logging.getLogger(__name__)
if logger_level.lower() == 'debug':
    log_data_updater.setLevel(logging.DEBUG)
if logger_level.lower() == 'error':
    log_data_updater.setLevel(logging.ERROR)
if logger_level.lower() == 'info':
    log_data_updater.setLevel(logging.INFO)
if logger_level.lower() == 'warning':
    log_data_updater.setLevel(logging.WARNING)
if logger_level.lower() == 'critical':
    log_data_updater.setLevel(logging.CRITICAL)
if logger_level == None:
    log_data_updater.setLevel(logging.NOTSET)
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)
fh = logging.FileHandler(filename=os.path.join(data_updater_log_path,
                                               data_updater_log_file),
                                               mode=file_mode,
                                               encoding='utf-8')
fh.setFormatter(formatter)
log_data_updater.handlers.clear()
log_data_updater.addHandler(sh)
log_data_updater.addHandler(fh)

class DataUpdater(object):
    def __init__(self):
        path = config.get_config()["temp_file"]
        self.temp_file = os.path.abspath(os.path.join(*path))
        if not os.path.exists(self.temp_file):
            os.makedirs(self.temp_file)
        self.set_token()
        self.instruments_service_connection = InstrumentsService(TOKEN=self.token)
        self.local_stored_instruments = self.get_local_stored_instruments_figi_list()

    def set_token(self):
        token = Token()
        self.token = token.access_token
        log_data_updater.debug(f'token {self.token[:10]}')

    def test(self):
        print('test')

    def get_local_stored_instruments_figi_list(self):
        '''Получим список инструментов в локальной БД
        '''
        db_data = self.get_local_db_instruments()
        figi_list = []
        for item in db_data:
            figi_list.append(item[0])
        return figi_list

    def update_accounts_in_local_db(self):
        '''Обновляет список счетов в локальной БД
        '''
        log_data_updater.debug(f'{__name__} -> RUN update_accounts_in_local_db()')
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
        log_data_updater.debug(f'{__name__} -> RUN update_positions_in_temp_file()')
        sql_query = ScriptNormalizer("accounts").select()
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        account_id_list = []
        for i in range(len(data)):
            account_id_list.append(str(data[i][0]))

        #Получим новые данные от сервера
        body = {"account_id_list":account_id_list}
        response_data = Operations(TOKEN=self.token, BODY=body)
        response_data_list = response_data.get_my_positions_by_account()

        log_data_updater.debug(f'{__name__} -> update_positions_in_temp_file() -> response_data_list:{response_data_list}')

        curent_time = datetime.datetime.now()
        positions = {"last_update":curent_time,
                     "positions_info":response_data_list}

        #если временная директория не существует, необходимо ее создать
        temp_dir = Path(os.path.dirname(self.temp_file))
        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)
        #Сохраним новые данные во временный файл
        #Откроем временный файл
        shelveFile = shelve.open(self.temp_file)
        shelveFile['positions_info'] = positions
        shelveFile.close()

    def get_local_db_instruments(self):
        '''Возвращает список инструментов сохраненных в локальной БД
        '''
        #Столбцы выборки
        cols_list=["figi"]
        #Создаем запрос к БД
        sql_query=ScriptNormalizer("instruments").select(cols_list=cols_list)
        log_data_updater.debug(f'{__name__} -> get_local_db_instruments() -> sql_query: {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        # log_data_updater.debug(f'{__name__} -> get_local_db_instruments data: {data}')
        return data

    def update_temp_file_with_curriencies(self):
        '''Метод Обновляет котировки валюты в локальном файле
        для прикладных нужд по следующему списку:
        "BBG0013HGFT4" - USD/RUB
        '''
        log_data_updater.debug(f'{__name__} -> RUN update_temp_file_with_curriencies()')
        request = MarketDataService(TOKEN=self.token)
        request.update_local_currencies()

    def update_db_with_new_shares(self):
        '''Обновляет локальную БД новыми инструментами типа stock
        '''
        #Получим актуальный список акций доступных на рынке
        shares_list=self.instruments_service_connection.get_shares_list()
        #Обновим БД если окажется что инструмента нет в локальной БД
        for instrument in shares_list:
            if instrument.figi not in self.local_stored_instruments:
                log_data_updater.info(f'{__name__} -> update_db_with_new_shares()-> instrument.figi: {instrument}')
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

    def update_db_with_new_bonds(self):
        '''Обновляет локальную БД новыми инструментами типа bond
        '''
        #Получим актуальный список облигаций доступных на рынке
        bond_list = self.instruments_service_connection.get_bonds_list()
        #Обновим БД если окажется что инструмента нет в локальной БД
        for instrument in bond_list:
            if instrument.figi not in self.local_stored_instruments:
                log_data_updater.info(f'{__name__} -> update_db_with_new_bonds() -> instrument.figi: {instrument}')
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

    def update_db_with_new_etf(self):
        '''Обновляет локальную БД новыми инструментами типа ETF
        '''
        #Получим актуальный список фондов доступных на рынке
        etf_list = self.instruments_service_connection.get_etf_list()
        #Обновим БД если окажется что инструмента нет в локальной БД
        for instrument in etf_list:
            if instrument.figi not in self.local_stored_instruments:
                log_data_updater.info(f'{__name__} -> update_db_with_new_etf() -> instrument.figi: {instrument}')
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

    def update_db_with_new_currencies (self):
        '''Обновляет локальную БД новыми инструментами типа currency
        '''
        #Получим актуальный список фондов доступных на рынке
        currency_list = self.instruments_service_connection.get_currencies_list()
        log_data_updater.info(f'{__name__} -> update_db_with_new_currencies() -> currency_list: {currency_list[:10]}')
        #Обновим БД если окажется что инструмента нет в локальной БД
        for instrument in currency_list:
            if instrument.figi not in self.local_stored_instruments:
                log_data_updater.info(f'{__name__} -> update_db_with_new_currencies() -> instrument.figi: {instrument}')
                instrument_json={"currency":instrument.currency,
                                 "figi":instrument.figi,
                                 "isin":instrument.isin,
                                 "lot":instrument.lot,
                                 "min_price_increment":instrument.lot,
                                 "ticker_name":instrument.name,
                                 "ticker":instrument.ticker,
                                 "instrument_type":"Currency"
                                }
                sql_query=ScriptNormalizer("instruments", new_data=instrument_json).insert()
                #Создание подключения к БД
                db_connection=DBIntegration()
                DBIntegration.script_executer_with_commit(db_connection,sql_query)

if __name__ == '__main__':

    data_updater = DataUpdater()

    while True:
        try:
            data_updater.update_positions_in_temp_file()
            data_updater.update_temp_file_with_curriencies()
            data_updater.update_accounts_in_local_db()
            data_updater.update_db_with_new_shares()
            data_updater.update_db_with_new_bonds()
            data_updater.update_db_with_new_etf()
            data_updater.update_db_with_new_currencies()

            time.sleep(config.get_config()["update_timer"])

        except KeyboardInterrupt:    #Без этой строчки код будет выполняться бесконечно при любом количестве ошибок
            log_data_updater.debug(f' Завершение работы: KeyboardInterrupt')
            is_running=False
            sys.exit(0)
        except Exception as e:
            log_data_updater.error(f'ERROR: {e}', exc_info=True)
            time.sleep(3)    #Перезапуск процесса скрипта спустя n сек
