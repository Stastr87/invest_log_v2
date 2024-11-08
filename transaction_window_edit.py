import json
import sys
from pprint import pprint
import time
from PySide6.QtWidgets import (QDialog, QCompleter, QVBoxLayout, QLineEdit)
from PySide6.QtCore import (Qt,QDate, QTime)
from ui.ui_transaction_form_edit import Ui_Dialog
from db_integration import DBIntegration
from sql_lib.script_normalizer import ScriptNormalizer

# import config
# from  my_logger import MyLogger
# logger_config = config.get_logger_config()
# log_file = logger_config['transaction_window_edit']
# log = MyLogger(log_file).new_logger

class TransactionWindowEdit(QDialog):
    def __init__(self):
        super(TransactionWindowEdit, self).__init__()
        self.ui  =  Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()
        self.connectUI()

    def init_UI(self):
        #При открытии окна делаем запрос к базе для получения выборки инструментов
        self.ticker_list, self.instrument_name_list = self.get_instruments_list()

    def connectUI(self):
        '''Описание сигналов для элементов интерфейса
        '''
        button_save  =  self.ui.Save_all
        #Сигнал принять результаты и закрыть окно
        button_save.clicked.connect(self.accept)
        button_save.clicked.connect(self.save_data)

        #Сигнал отменить результаты и закрыть окно
        button_cancel  =  self.ui.Cancel
        button_cancel.clicked.connect(self.reject)

    def set_brocker_accounts_list(self):
        # Метод динамически создает список элементов для объекта QComboBox
        # Данные о счетах храняться в БД

        search_template = {"brocker_name":f"{self.ui.Brocker.currentText()}"}
        sql_query = ScriptNormalizer("accounts").select(LIKE = search_template)
        # log.debug(f'{__name__}. {sql_query}')

        #Создание подключения к БД
        db_connection = DBIntegration()

        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        #log.debug(f'{__name__}.data: {data}')
        account_names_list = []
        for i in range(len(data)):
            account_names_list.append(data[i][1])

        self.ui.Brocker_account.addItems(account_names_list)
        for i in range(len(account_names_list)):
            self.ui.Brocker_account.setItemData(i, account_names_list[i],Qt.BackgroundRole)

    def get_instrument_all_data(self):
        #Шаблон значений в ячейках для выборки поиск по всем слобцам
        search_template = {"ticker":self.ui.ticker_edit.text()}
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("instruments").select(LIKE = search_template)
        # log.debug(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        # log.debug(f'{__name__}.data: {data}')
        self.ui.Currency.setText(data[0][8])
        self.ui.Currency.setReadOnly(True)

    def get_instruments_list(self):
        #Столбцы выборки
        cols_list = ["ticker","ticker_name"]
        #Параметр сортировки
        order = ["ticker_name","ASC"]
        #Шаблон значений в ячейках для выборки поиск по всем таблицам
        ##
        ##text = self.ui.ticker_edit.text()
        ##search_template = {"ticker_name":f"%{text}%",
        ##                 "ticker":f"%{text}%"}
        #Ограничение вариантов выборки
        limit = 100
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("instruments").select(cols_list = cols_list, ORDER = order)
        # log.debug(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        #log.debug(f'{__name__}.data: {data}')
        ticker_list = []
        instrument_name_list = []
        for item in data:
            value1, value2 = item
            ticker_list.append(value1)
            instrument_name_list.append(value2)

        return ticker_list, instrument_name_list

    def get_ticker(self):
        #Столбцы выборки
        cols_list = ["ticker","instrument_type"]
        search_template = {"ticker_name":self.ui.instrument_name.text()}
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("instruments").select(cols_list = cols_list, LIKE = search_template)
        # log.info(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        # log.debug(f'{__name__}.data: {data}')

        ticker_tupl = data[0]
        ticker = ticker_tupl[0]
        instrument_type = ticker_tupl[1]
        if instrument_type != 'Bond':
            self.ui.nkd_edit.setEnabled(False)
        # log.info(f'{__name__}.ticker: {ticker}')
        self.ui.ticker_edit.setText(ticker)
        self.nkd  =  QLineEdit()

    def get_instrument_attributes(self, figi):
        where = {"figi":figi}
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("instruments").select(WHERE = where)
        # log.info(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        # log.info(f'{__name__}.data: {data}')
        try:
            instrument_name_tupl = data[0]
            instrument_name = instrument_name_tupl[1]
            instrument_ticker = instrument_name_tupl[2]
            currency = instrument_name_tupl[8]
        except:
            instrument_name_tupl = None
            instrument_name = None
            instrument_ticker = None
            currency = None

        # log.info(f'{__name__}.instrument_name, instrument_ticker: {instrument_name, instrument_ticker}')

        return instrument_name, instrument_ticker, currency

    # Описание слотов
    #
    # Начало

    def set_title(self, title):
        self.setWindowTitle(title)

    def save_data(self):
        def get_ticker_guid(ticker):
            #Шаблон значений в ячейках для выборки поиск по всем слобцам
            search_template = {"ticker":ticker}
            #Создаем запрос к БД
            sql_query = ScriptNormalizer("instruments").select(LIKE = search_template)
            # log.debug(f'{__name__}. {sql_query}')
            #Создание подключения к БД
            db_connection = DBIntegration()
            #Отправка запроса
            data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
            # log.debug(f'{__name__}.data: {data}')
            return data[0][0]

        def get_account_id(account_name):
            search_template = {"account_name":account_name}
            sql_query = ScriptNormalizer("accounts").select(LIKE = search_template)
            # log.debug(f'{__name__}. {sql_query}')
            #Создание подключения к БД
            db_connection = DBIntegration()
            #Отправка запроса
            data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
            # log.debug(f'{__name__}.data: {data}')
            return data[0][0]

        #Получить данные из полей формы
        data = {"date_time":self.ui.dateTimeEdit.text(),
              "transaction_type": self.ui.transaction_type.text(),
              "ticker_guid": get_ticker_guid(self.ui.ticker_edit.text()),
              "brocker": self.ui.brocker_name.text(),
              "brocker_account": str(get_account_id(self.ui.account_name.text())),
              "ticker": self.ui.ticker_edit.text(),
              "currency": self.ui.Currency.text(),
              "price": self.ui.price_edit.text().replace(',','.'),
              "volume": self.ui.volume_edit.text(),
              "fee": self.ui.fee_edit.text().replace(',','.'),
              "memo": self.ui.description.toPlainText(),
              "nkd": self.ui.nkd_edit.text().replace(',','.')}

        if self.ui.nkd_edit.text() == '':
            del data['nkd']
        if self.ui.fee_edit.text() == '':
            data['fee']  =  0

        #Для отладки
        #with open('store_data.json','w',encoding = 'utf-8') as file:
        #    file.write(json.dumps(data, ensure_ascii = False,indent = 4))

        sender  =  self.sender()
        # log.debug(f'btn "{sender.text()}" Clicked!')

        sql_query = ScriptNormalizer("transactions", new_data = data).insert()
        db_connection = DBIntegration()
        DBIntegration.script_executer_with_commit(db_connection,sql_query)

    # Описание слотов
    #
    # Конец

