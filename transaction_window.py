import json
import sys
from pprint import pprint
import time
from PySide6.QtWidgets import (QDialog, QCompleter, QVBoxLayout, QLineEdit)
from PySide6.QtCore import (Qt,QDate, QTime)
from ui.ui_transaction_form import Ui_Dialog
from db_integration import DBIntegration
from sql_lib.script_normalizer import ScriptNormalizer




class TransactionWindow(QDialog):
    def __init__(self):
        '''Инициализация окна добавления или редактирования транзакции'''
        super(TransactionWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()
        self.connectUI()


    def init_UI(self):
        # При открытии окна делаем запрос к базе для получения выборки инструментов
        self.ticker_list, self.instrument_name_list=self.get_instruments_list()
        #Задаем текущую дату и время в поле времени
        qdate = QDate.currentDate()
        qtime = QTime.currentTime()
        self.ui.dateTimeEdit.setDate(qdate)
        self.ui.dateTimeEdit.setTime(qtime)
        #Задаем порядок перехода по элементам кнопкой tab
        self.ui.dateTimeEdit.setTabOrder(self.ui.dateTimeEdit, self.ui.Transactio_type)
        self.ui.Transactio_type.setTabOrder(self.ui.Transactio_type, self.ui.Brocker)
        self.ui.Brocker.setTabOrder(self.ui.Brocker, self.ui.Brocker_account)
        self.ui.Brocker_account.setTabOrder(self.ui.Brocker_account, self.ui.ticker_edit)
        self.ui.ticker_edit.setTabOrder(self.ui.ticker_edit, self.ui.price_edit)
        self.ui.instrument_name.setTabOrder(self.ui.instrument_name, self.ui.price_edit)
        self.ui.price_edit.setTabOrder(self.ui.price_edit, self.ui.volume_edit)
        self.ui.volume_edit.setTabOrder(self.ui.volume_edit, self.ui.fee_edit)
        self.ui.fee_edit.setTabOrder(self.ui.fee_edit, self.ui.nkd_edit)
        self.ui.nkd_edit.setTabOrder(self.ui.nkd_edit, self.ui.description)
        self.ui.description.setTabOrder(self.ui.description, self.ui.Cancel)
        self.ui.Cancel.setTabOrder(self.ui.Cancel, self.ui.Save_all)

    def connectUI(self):
        '''Описание сигналов для элементов интерфейса
        '''
        # Сфоримровать список счетов у выбранного брокера
        self.ui.Brocker.textActivated.connect(self.set_brocker_accounts_list)

        # Выдать результаты поиска тикера или
        # имени инструмента в БД по введеному шаблону
        self.ui.ticker_edit.textEdited.connect(self.create_ticker_edit_completer)
        self.ui.ticker_edit.editingFinished.connect(self.get_instrument_name)
        self.ui.ticker_edit.editingFinished.connect(self.get_instrument_all_data)

        self.ui.instrument_name.textEdited.connect(self.create_instrument_name_completer)
        self.ui.instrument_name.editingFinished.connect(self.get_ticker)
        self.ui.instrument_name.editingFinished.connect(self.get_instrument_all_data)

        button_save = self.ui.Save_all
        #Сигнал принять результаты и закрыть окно
        button_save.clicked.connect(self.accept)
        button_save.clicked.connect(self.save_data)

        #Сигнал отменить результаты и закрыть окно
        button_cancel = self.ui.Cancel
        button_cancel.clicked.connect(self.reject)

    def set_brocker_accounts_list(self):
        # Метод динамически создает список элементов для объекта QComboBox
        # Данные о счетах храняться в БД

        search_template={"brocker_name":f"{self.ui.Brocker.currentText()}"}
        sql_query=ScriptNormalizer("accounts").select(LIKE=search_template)
        # log.debug(f'{__name__}. {sql_query}')

        #Создание подключения к БД
        db_connection=DBIntegration()

        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        #log.debug(f'{__name__}.data: {data}')
        account_names_list=[]
        for i in range(len(data)):
            account_names_list.append(data[i][1])

        self.ui.Brocker_account.addItems(account_names_list)
        for i in range(len(account_names_list)):
            self.ui.Brocker_account.setItemData(i, account_names_list[i],Qt.BackgroundRole)

    def get_instrument_all_data(self):
        #Шаблон значений в ячейках для выборки поиск по всем слобцам
        search_template={"ticker":self.ui.ticker_edit.text()}
        #Создаем запрос к БД
        sql_query=ScriptNormalizer("instruments").select(LIKE=search_template)
        # log.debug(f'{__name__} -> get_instrument_all_data() -> sql_query: {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        # log.debug(f'{__name__} -> get_instrument_all_data() -> data: {data}')
        self.ui.Currency.setText(data[0][8])
        self.ui.Currency.setReadOnly(True)

    def get_instruments_list(self):
        #Столбцы выборки
        cols_list=["ticker","ticker_name"]
        #Параметр сортировки
        order=["ticker_name","ASC"]
        #Шаблон значений в ячейках для выборки поиск по всем таблицам
        ##text=self.ui.ticker_edit.text()
        ##search_template={"ticker_name":f"%{text}%",
        ##                 "ticker":f"%{text}%"}
        #Ограничение вариантов выборки
        limit=100
        #Создаем запрос к БД
        sql_query=ScriptNormalizer("instruments").select(cols_list=cols_list, ORDER=order)
        # log.debug(f'{__name__} -> get_instruments_list() -> sql_query: {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        ticker_list=[]
        instrument_name_list=[]
        for item in data:
            value1, value2=item
            ticker_list.append(value1)
            instrument_name_list.append(value2)

        return ticker_list, instrument_name_list

    def get_ticker(self):
        #Столбцы выборки
        cols_list=["ticker","instrument_type"]
        search_template={"ticker_name":self.ui.instrument_name.text()}
        #Создаем запрос к БД
        sql_query=ScriptNormalizer("instruments").select(cols_list=cols_list, LIKE=search_template)
        # log.info(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        # log.debug(f'{__name__}.data: {data}')

        ticker_tupl=data[0]
        ticker=ticker_tupl[0]
        instrument_type=ticker_tupl[1]
        if instrument_type!='Bond':
            self.ui.nkd_edit.setEnabled(False)
        # log.info(f'{__name__}.ticker: {ticker}')
        self.ui.ticker_edit.setText(ticker)
        self.nkd = QLineEdit()

    def get_instrument_name(self):
        #Столбцы выборки
        cols_list=["ticker_name"]
        #Параметр сортировки
        order=["ticker_name","ASC"]
        #Шаблон значений в ячейках для выборки поиск по всем таблицам
        search_template={"ticker":f"{self.ui.ticker_edit.text()}"}
        #Ограничение вариантов выборки
        limit=100
        #Создаем запрос к БД
        sql_query=ScriptNormalizer("instruments").select(cols_list=cols_list, ORDER=order, LIKE=search_template)
        # log.info(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        # log.info(f'{__name__}.data: {data}')

        instrument_name_tupl=data[0]
        instrument_name=instrument_name_tupl[0]
        # log.info(f'{__name__}.instrument_name: {instrument_name}')
        self.ui.instrument_name.setText(instrument_name)


    def get_ticker_guid(self, ticker):
        #Шаблон значений в ячейках для выборки поиск по всем слобцам
        search_template={"ticker":ticker}
        #Создаем запрос к БД
        sql_query=ScriptNormalizer("instruments").select(LIKE=search_template)
        # log.debug(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        # log.debug(f'{__name__}.data: {data}')
        return data[0][0]

    def get_account_id(self,account_name):
        search_template={"account_name":account_name}
        sql_query=ScriptNormalizer("accounts").select(LIKE=search_template)
        # log.debug(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        # log.debug(f'{__name__}.data: {data}')
        return data[0][0]


    # Описание слотов
    #
    # Начало
    def create_instrument_name_completer(self):
        #Создаем поле для отображения вариантов
        layout = QVBoxLayout(self.ui.instrument_name)
        completer = QCompleter(self.instrument_name_list)
        #Отключаем чувствительность к регистру
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.instrument_name.setCompleter(completer)
        self.setLayout(layout)

    def create_ticker_edit_completer(self):
        #Создаем поле для отображения вариантов
        layout = QVBoxLayout(self.ui.ticker_edit)
        completer = QCompleter(self.ticker_list)
        #Отключаем чувствительность к регистру
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.ticker_edit.setCompleter(completer)
        self.setLayout(layout)

    def set_title(self, title):
        self.setWindowTitle(title)

    def save_data(self):
        Brocker_account=self.ui.Brocker_account.currentText()
        ticker=self.ui.ticker_edit.text()
        #Получить данные из полей формы
        data={"date_time": self.ui.dateTimeEdit.text(),
              "transaction_type": self.ui.Transactio_type.currentText(),
              "ticker_guid": self.get_ticker_guid(ticker),
              "brocker": self.ui.Brocker.currentText(),
              "brocker_account": str(self.get_account_id(Brocker_account)),
              "ticker": self.ui.ticker_edit.text(),
              "currency": self.ui.Currency.text(),
              "price": self.ui.price_edit.text().replace(',','.'),
              "volume": self.ui.volume_edit.text(),
              "fee": self.ui.fee_edit.text().replace(',','.'),
              "memo": self.ui.description.toPlainText(),
              "nkd": self.ui.nkd_edit.text().replace(',','.')}

        if self.ui.nkd_edit.text()=='':
            del data['nkd']

        #Для отладки
        #with open('store_data.json','w',encoding='utf-8') as file:
        #    file.write(json.dumps(data, ensure_ascii=False,indent=4))

        sender = self.sender()
        # log.debug(f'btn "{sender.text()}" Clicked!')
        label_text=self.ui.label.text()
        # log.debug(f'{__name__} -> save_data() -> self.ui.label.text(): {self.ui.label.text()}')
        if "Добавить сведения об операции" in label_text:
            sql_query=ScriptNormalizer("transactions", new_data=data).insert()
            db_connection=DBIntegration()
            DBIntegration.script_executer_with_commit(db_connection,sql_query)
        if "Редактировать сведения об операции" in label_text:
            transaction_id=label_text[38:]
            # log.debug(f'{__name__} -> transaction_id: {transaction_id}')
            sql_query=ScriptNormalizer("transactions", new_data=data).update(WHERE={'transaction_id':transaction_id})
            db_connection=DBIntegration()
            DBIntegration.script_executer_with_commit(db_connection,sql_query)


    # Описание слотов
    #
    # Конец

