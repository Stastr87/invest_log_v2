from PySide6.QtWidgets import QWidget
from ui.ui_test_panel import QWidget, Ui_Form
from db_integration import DBIntegration
from sql_lib.script_normalizer import ScriptNormalizer
import auth.token as Auth
from services.operations_service.operations_service import Operations
from services.accounts_service.accounts_service import Accounts
#from openapi_client import openapi

from pprint import pprint
import shelve
import datetime
import os
from pathlib import Path

import my_logger
log = my_logger.setup_applevel_logger(file_name = 'test_panel.log')

class TestPanel_Window(QWidget):
    def __init__(self):
        super(TestPanel_Window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Тестовая панель")
        self.ui.test_button.click

        button_test_button = self.ui.test_button
        button_test_button.clicked.connect(self.get_positions_info)

        button_load_position_data = self.ui.load_position_data
        button_load_position_data.clicked.connect(self.load_positions_info)

        button_update_accounts=self.ui.update_accounts
        button_update_accounts.clicked.connect(self.update_accounts)

        button_update_instruments = self.ui.update_instruments
        button_update_instruments.clicked.connect(self.update_instruments)

    def get_token(self):
        token_object=Auth.Token()
        token_object.token=token_object.get_trading_token_from_file()
        return token_object.token

    def get_account_id_list(self):
        '''Возвращает список счетов из локальной БД.
        '''
        sql_query=ScriptNormalizer("accounts").select()
        log.debug(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)

        account_id_list=[]
        for i in range(len(data)):
            account_id_list.append(str(data[i][0]))
        log.debug(f'{__name__}. -> account_id_list: {account_id_list}')
        return account_id_list


    def get_positions_info(self):
        account_id_list=self.get_account_id_list()
        body={"account_id_list":account_id_list}
        request=Operations(TOKEN=self.get_token(),BODY=body)
        response_data_list=request.get_my_positions_by_account()
        curent_time=datetime.datetime.now()
        positions={"last_update":curent_time,
                   "positions_info":response_data_list}
        #Сохраним данные во временном файле
        #Используется библиотека pathlib для
        #корректного присвоения путей в разных ОС
        temp_dir=Path("temp_data")
        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)
        temp_file=temp_dir/"temp"
        shelveFile=shelve.open(temp_file)
        shelveFile['positions_info']=positions
        shelveFile.close()

    def load_positions_info(self):
        temp_file=Path("temp_data/temp")
        shelveFile=shelve.open(temp_file)
        positions_storage=shelveFile['positions_info']
        pprint(f"{positions_storage.keys()}")
        last_update=positions_storage['last_update']
        positions_info=positions_storage['positions_info']
        pprint(f"last_update {last_update}")
        for item in positions_info:
            pprint(item["account_id"])
            pprint(item["positions"].securities)


    def get_accounts(self):
        sql_query=ScriptNormalizer("accounts").select()
        log.debug(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        log.debug(f'{__name__} -> get_accounts data: {data}')
        return data

    def update_accounts(self):
        '''Обновляет список счетов в локальной БД
        '''
        db_data=self.get_accounts()
        accounts_id_list=[]
        for item in db_data:
            accounts_id_list.append(str(item[0]))

        request=Accounts(TOKEN=self.get_token())
        response_data=request.get_my_accounts()
        log.debug(f'{__name__} -> update_accounts: response_data {response_data}')

        for item in response_data:
            if item["account_id"] not in accounts_id_list:
                sql_query=ScriptNormalizer("accounts", new_data=item).insert()
                #Создание подключения к БД
                db_connection=DBIntegration()
                DBIntegration.script_executer_with_commit(db_connection,sql_query)

    def get_local_db_instruments(self):
        #Столбцы выборки
        cols_list=["figi"]
        #Создаем запрос к БД
        sql_query=ScriptNormalizer("instruments").select(cols_list=cols_list)
        log.info(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        #log.info(f'{__name__} -> get_local_db_instruments data: {data}')
        return data

    '''
    def update_instruments(self):
        """Обновление списка инструментов в локальной БД
        """
        db_data=self.get_local_db_instruments()
        figi_list=[]
        for item in db_data:
            figi_list.append(item[0])

        log.info(f'{__name__} -> update_instruments figi_list[0]: {figi_list[0]}')

        client = openapi.api_client(self.get_token())

        shares_list_data = client.market.market_stocks_get()
        shares_list=shares_list_data.payload.instruments

        bonds_list_data=client.market.market_bonds_get()
        bonds_list=bonds_list_data.payload.instruments

        etf_list_data = client.market.market_etfs_get()
        etf_list=etf_list_data.payload.instruments

        instruments_list=shares_list+bonds_list+etf_list
        for instrument in instruments_list:
            if instrument.figi not in figi_list:
                log.info(f'{__name__} -> update_instruments instrument.figi: {instrument}')
                instrument_json={"currency":instrument.currency,
                                 "figi":instrument.figi,
                                 "isin":instrument.isin,
                                 "lot":instrument.lot,
                                 "min_price_increment":instrument.lot,
                                 "ticker_name":instrument.name,
                                 "ticker":instrument.ticker,
                                 "instrument_type":instrument.type
                                 }

                sql_query=ScriptNormalizer("instruments", new_data=instrument_json).insert()
                #Создание подключения к БД
                db_connection=DBIntegration()
                DBIntegration.script_executer_with_commit(db_connection,sql_query)
    '''