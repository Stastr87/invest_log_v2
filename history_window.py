import platform, sys, os
from PySide6.QtGui import QColor
from PySide6.QtCore import QDate, QTime, Qt, Signal
from PySide6.QtWidgets import (QWidget,QTableWidget, QTableWidgetItem, QButtonGroup,
                               QCompleter, QVBoxLayout, QLineEdit)
from ui.ui_history_window import QWidget, Ui_Form
from transaction_window import TransactionWindow
from transaction_window_edit import TransactionWindowEdit
from db_integration import DBIntegration
from sql_lib.script_normalizer import ScriptNormalizer
from lib.tink_integration.operations_servise import Operations, OperationTypes
from auth.token import Token

import config
logger_config = config.get_logger_config()

if 'wind' in platform.system():
    history_window_log_path = logger_config['path']
else:
    history_window_log_path = logger_config['alternative_path']

history_window_log_file = logger_config['history_window']['name']
file_mode = logger_config['history_window']['mode']
logger_level = logger_config['history_window']['level']

import logging
# Настройка логирования
log_history_window = logging.getLogger(__name__)
if logger_level.lower() == 'debug':
    log_history_window.setLevel(logging.DEBUG)
if logger_level.lower() == 'error':
    log_history_window.setLevel(logging.ERROR)
if logger_level.lower() == 'info':
    log_history_window.setLevel(logging.INFO)
if logger_level.lower() == 'warning':
    log_history_window.setLevel(logging.WARNING)
if logger_level.lower() == 'critical':
    log_history_window.setLevel(logging.CRITICAL)
if logger_level == None:
    log_history_window.setLevel(logging.NOTSET)

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)
fh = logging.FileHandler(filename=os.path.join(history_window_log_path, 
                                               history_window_log_file), 
                         mode=file_mode,
                         encoding='utf-8')
fh.setFormatter(formatter)
log_history_window.handlers.clear()
log_history_window.addHandler(sh)
log_history_window.addHandler(fh)



from services.data_converter import DataConverter
# Создадим экземпляр класса DataConverter() для последующей конвертации данных в коде
converter = DataConverter()

class HistoryWindow(QWidget):

    resized = Signal()
    def __init__(self, parent=None):
        super(HistoryWindow, self).__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Журнал сделок")
        self.connectUi()
        self.resized.connect(self.resize_function)
        self.set_token()
        # log.info(f'{self.__class__.__name__} initialized!!!')

    def set_token(self):
        token = Token()
        self.token = token.access_token

    def resizeEvent(self, event):
            '''Действие при изменении размера окна

            DOC: https://doc.qt.io/qtforpython-6/overviews/signalsandslots.html#signals-slots
            '''
            self.resized.emit()
            return super(HistoryWindow, self).resizeEvent(event)

    def connectUi(self):
        '''Формирование интефеса и заполнение данными
        '''
        qdate = QDate.currentDate()
        self.ui.start_date.setDate(QDate(qdate.year(),qdate.month(),qdate.day()))
        self.ui.end_date.setDate(QDate(qdate.year(),qdate.month(),qdate.day()))

        self.ticker_list, self.instrument_name_list=self.get_instruments_list()
        self.ui.results_table.setStyleSheet(u"QTableView{background-color:rgb(220,220,220);\n"
                                            u"border: 2px solid;\n"
                                            u"border-radius: 7px;\n"
                                            u"border-color: rgb(205, 205, 205);}")

        # Описание сигналов для элементов интерфейса
        operations_period_radio_button = self.ui.operations_period
        all_operations_radio_button = self.ui.all_operations
        radio_button_group = QButtonGroup()
        radio_button_group.addButton(all_operations_radio_button,1)
        radio_button_group.addButton(operations_period_radio_button,2)
        operations_period_radio_button.setChecked(True)

        # Выдать результаты поиска тикера или
        # имени инструмента в БД по введеному шаблону
        self.ui.ticker_edit.textEdited.connect(self.create_ticker_edit_completer)
        self.ui.ticker_edit.editingFinished.connect(self.set_instrument_name)
        self.ui.instrument_name.textEdited.connect(self.create_instrument_name_completer)
        self.ui.instrument_name.editingFinished.connect(self.set_ticker)
        self.ui.Brocker.textActivated.connect(self.set_brocker_accounts_list)

        button_add = self.ui.Add_transaction
        button_add.clicked.connect(self.open_transaction_form)

        button_delete = self.ui.Delete_selection
        button_delete.clicked.connect(self.the_button_was_clicked)

        button_db_query = self.ui.db_query
        button_db_query.clicked.connect(self.the_button_was_clicked)
        button_db_query.clicked.connect(self.create_invest_log_table_v2)

        button_brocker_query = self.ui.brocker_query
        button_brocker_query.clicked.connect(self.the_button_was_clicked)
        button_brocker_query.clicked.connect(self.create_operation_info_table)

        button_Edit_transaction = self.ui.Edit_transaction
        button_Edit_transaction.clicked.connect(self.the_button_was_clicked)
        button_Edit_transaction.clicked.connect(self.edit_transaction_from_local_db)

        button_add_transaction_from_table = self.ui.add_transaction_from_table
        button_add_transaction_from_table.clicked.connect(self.the_button_was_clicked)
        button_add_transaction_from_table.clicked.connect(self.edit_transaction_with_safe_new_one)

    def set_brocker_accounts_list(self):
        '''
        Метод динамически создает список элементов для объекта QComboBox
        Данные о счетах храняться в БД'''

        #Очистим комбобокс если ранее в нем был какой-то список
        self.ui.Brocker_account.clear()

        #Сформируем актуальный список счетов из локальной БД
        search_template = {"brocker_name":f"{self.ui.Brocker.currentText()}"}
        sql_query=ScriptNormalizer("accounts").select(LIKE=search_template)
        #log.debug(f'{__name__} -> set_brocker_accounts_list -> {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        #log.debug(f'{__name__}.data: {data}')

        account_names_list = list()
        for i in range(len(data)):
            account_names_list.append(data[i][1])
        #Добавим в начало списока элемент "Все" на случай когда понадобится получить
        #данные по всем счетам
        account_names_list.insert(0,'Все')

        self.ui.Brocker_account.addItems(account_names_list)
        for i in range(len(account_names_list)):
            self.ui.Brocker_account.setItemData(i, account_names_list[i],Qt.BackgroundRole)

        #По умолчанию в комбобоксе выбраны все счета
        self.ui.Brocker_account.setCurrentIndex(0)

    def get_instruments_list(self):
        '''Функция возвращает 2 независимых списка
        тикеров и названий инстрементов
        '''
        #Столбцы выборки
        cols_list=["ticker","ticker_name"]
        #Параметр сортировки
        order=["ticker_name","ASC"]
        #Шаблон значений в ячейках для выборки поиск по всем таблицам
        #Ограничение вариантов выборки
        limit = 100
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("instruments").select(cols_list=cols_list,
                                                         ORDER=order)
        #log.debug(f'{__name__}. {sql_query}')
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

    def set_ticker(self):
        '''Задает текст в интерфейсе окна
        '''
        #Столбцы выборки
        cols_list = ["ticker","instrument_type"]
        search_template = {"ticker_name":self.ui.instrument_name.text()}
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("instruments").select(cols_list=cols_list, LIKE=search_template)
        #log.info(f'{__name__} -> {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        #log.debug(f'{__name__} -> data: {data}')
        ticker_tupl = data[0]
        ticker = ticker_tupl[0]
        #log.info(f'{__name__} -> ticker: {ticker}')
        self.ui.ticker_edit.setText(ticker)

    def create_instrument_name_completer(self):
        '''Формирование комплитера отображения вариантов
        '''
        layout = QVBoxLayout(self.ui.instrument_name)
        completer = QCompleter(self.instrument_name_list)
        #Отключаем чувствительность к регистру
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.instrument_name.setCompleter(completer)
        self.setLayout(layout)

    def create_ticker_edit_completer(self):
        '''Формирование комплитера отображения вариантов
        '''
        layout = QVBoxLayout(self.ui.ticker_edit)
        completer = QCompleter(self.ticker_list)
        #Отключаем чувствительность к регистру
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.ticker_edit.setCompleter(completer)
        self.setLayout(layout)

    def get_instrument_all_data(self):
        '''Возвращает кортеж из всех данных по запрошенному инструменту
        '''
        #Шаблон значений в ячейках для выборки поиск по всем слобцам
        search_template = {"ticker":self.ui.ticker_edit.text()}
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("instruments").select(LIKE=search_template)
        #log.debug(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        #log.debug(f'{__name__}.data: {data}')

    def set_instrument_name(self):
        '''Возвращает и задает имя инструмента в интерфейсе окна
        '''
        #Столбцы выборки
        cols_list = ["ticker_name"]
        #Шаблон значений в ячейках для выборки поиск по всем таблицам
        search_template = {"ticker":self.ui.ticker_edit.text()}
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("instruments").select(cols_list=cols_list, LIKE=search_template)
        #log.info(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        instrument_name_tupl = data[0]
        instrument_name = instrument_name_tupl[0]
        self.ui.instrument_name.setText(instrument_name)

    def get_account_dict(self):
        '''Возвращает 2 независимых словаря вида
        {"account_id":"account_name"}
        {"account_id":"brocker_name"}
        '''
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("accounts").select()
        # log.info(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)

        account_id, account_name, brocker_name = list(), list(), list()
        for item in data:
           account_id.append(str(item[0]))
           account_name.append(item[1])
           brocker_name.append(item[2])
        #Объединим списки в словари
        account_dict = dict(zip((account_id), account_name))
        brocker_dict = dict(zip((account_id), brocker_name))
        return account_dict, brocker_dict

    def get_account_id_list(self):
        ''' Метод возвращает список id аккаунтов для объекта QComboBox
        '''
        # Данные о счетах храняться в БД
        sql_query = ScriptNormalizer("accounts").select()
        #log.debug(f'{__name__}. {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)

        account_id_list = list()
        for i in range(len(data)):
            account_id_list.append(str(data[i][0]))
        #log.debug(f'{__name__}. -> account_id_list: {account_id_list}')
        return account_id_list

    def get_brocker_log(self, account_id_list, start_date,end_date):
        '''Формирует таблицу по данным полученным от сервера.
        Столбцы таблицы:
        0 - идентификатор таблицы
        1 - "account_id",
        2 - "account_name",
        3 - "brocker_name",
        4 - "id",
        5 - "parent_operation_id",
        6 - "currency",
        7 - "price",
        8 - "payment",
        9 - "state",
        10 - "quantity",
        11 - "quantity_rest",
        12 - "figi",
        13 - "instrument_type",
        14 - "date",
        15 - "type",
        16 - "operation_type",
        17 - "trades",
        18 - "asset_uid",
        19 - "position_uid",
        20 - "instrument_uid"
        21 - "operation_enum"
        '''
        accounts_info, brocker_info = self.get_account_dict()
        #log.debug(f'{__name__} -> accounts_info {accounts_info}')
        body = {"account_id_list":account_id_list,
               "start":f'{start_date}T00:00:00+0400',
               "end":f'{end_date}T23:59:59+0400',
               "state":1,
               "figi":""}

        request = Operations(TOKEN=self.token,BODY=body)
        response_data_list = request.get_my_operations_by_account()
        #log.debug(f'{__name__} get_brocker_log -> type(response_data): {type(response_data_list)}')
        operation_data_list = []
        for i in range(len(account_id_list)):
            for operation in response_data_list[i].operations:
                    # log.debug(f'{__name__} get_brocker_log -> operation: {operation}')
                    operation_data={"account_id":account_id_list[i],
                                    "account_name":accounts_info[account_id_list[i]],
                                    #В перспективе если потребуется указать другого брокера доработать таблицу
                                    "brocker_name":'T',
                                    "id":operation.id,
                                    "parent_operation_id":operation.parent_operation_id,
                                    "currency":operation.currency,
                                    "payment":operation.payment,
                                    "price":operation.price,
                                    "state":str(operation.state),
                                    "quantity":operation.quantity,
                                    "quantity_rest":operation.quantity_rest,
                                    "figi":operation.figi,
                                    "instrument_type":operation.instrument_type,
                                    "date":str(operation.date),
                                    "type":operation.type,
                                    "operation_type":str(operation.operation_type),
                                    "trades":str(operation.trades),
                                    "asset_uid":operation.asset_uid,
                                    "position_uid":operation.position_uid,
                                    "instrument_uid":operation.instrument_uid,
                                    "operation_enum":operation}
                    #log.debug(f'{__name__} -> account_id_list[{i}] {operation_data}')
                    operation_data_list.append(operation_data)

        #Создаем таблицу
        #Очищаем таблицу если до этого она была не пуста
        self.ui.results_table.clear()
        if len(operation_data_list) == 0:
            self.ui.results_table.setRowCount(1)
            self.ui.results_table.setColumnCount(1)
            item_message = QTableWidgetItem('Список операций пуст')
            self.ui.results_table.setItem(0, 0, item_message)
            self.ui.results_table.horizontalHeader().hide()
            self.ui.results_table.verticalHeader().hide()
            self.ui.results_table.setShowGrid(False)

        else:
            self.ui.results_table.setRowCount(len(operation_data_list))
            self.ui.results_table.setColumnCount(len(operation_data_list[0])+1)

            labels_list=["table",
                         "account_id",
                         "account_name",
                         "brocker_name",
                         "id",
                         "parent_operation_id",
                         "currency",
                         "price",
                         "payment",
                         "state",
                         "quantity",
                         "quantity_rest",
                         "figi",
                         "instrument_type",
                         "date",
                         "type",
                         "operation_type",
                         "trades",
                         "asset_uid",
                         "position_uid",
                         "instrument_uid",
                         "operation_enum"]

            for i in range(len(operation_data_list)):
                item_table = QTableWidgetItem("brocker_log")
                item_account_id = QTableWidgetItem(operation_data_list[i]["account_id"])
                item_account_name = QTableWidgetItem(operation_data_list[i]["account_name"])
                item_brocker_name = QTableWidgetItem(operation_data_list[i]["brocker_name"])
                item_id = QTableWidgetItem(operation_data_list[i]["id"])
                item_parent_operation_id = QTableWidgetItem(operation_data_list[i]["parent_operation_id"])
                item_currency = QTableWidgetItem(operation_data_list[i]["currency"])
                payment = converter.tink_money_value_to_float(operation_data_list[i]["payment"])
                item_payment = QTableWidgetItem(str(round(payment,2)))
                item_state = QTableWidgetItem(str(operation_data_list[i]["state"]))
                price = converter.tink_money_value_to_float(operation_data_list[i]["price"])
                item_price = QTableWidgetItem(str(round(price,4)))
                item_quantity = QTableWidgetItem(str(operation_data_list[i]["quantity"]))
                item_quantity_rest = QTableWidgetItem(str(operation_data_list[i]["quantity_rest"]))
                item_figi = QTableWidgetItem(operation_data_list[i]["figi"])
                item_instrument_type = QTableWidgetItem(operation_data_list[i]["instrument_type"])
                item_date = QTableWidgetItem(str(operation_data_list[i]["date"]))
                item_type = QTableWidgetItem(str(operation_data_list[i]["type"]))

                operation_type_enum = OperationTypes(int(operation_data_list[i]["operation_type"]))
                item_operation_type = QTableWidgetItem(operation_type_enum.get_translation())
                item_operation_type_enum = QTableWidgetItem(str(operation_type_enum.value))

                item_trades = QTableWidgetItem(str(operation_data_list[i]["trades"]))
                item_asset_uid = QTableWidgetItem(operation_data_list[i]["asset_uid"])
                item_position_uid = QTableWidgetItem(operation_data_list[i]["position_uid"])
                item_instrument_uid = QTableWidgetItem(operation_data_list[i]["instrument_uid"])


                self.ui.results_table.setItem(i, 0, item_table)
                self.ui.results_table.setItem(i, 1, item_account_id)
                self.ui.results_table.setItem(i, 2, item_account_name)
                self.ui.results_table.setItem(i, 3, item_type)
                self.ui.results_table.setItem(i, 4, item_id)
                self.ui.results_table.setItem(i, 5, item_parent_operation_id)
                self.ui.results_table.setItem(i, 6, item_currency)
                self.ui.results_table.setItem(i, 7, item_price)
                self.ui.results_table.setItem(i, 8, item_payment)
                self.ui.results_table.setItem(i, 9, item_state)
                self.ui.results_table.setItem(i, 10, item_quantity)
                self.ui.results_table.setItem(i, 11, item_quantity_rest)
                self.ui.results_table.setItem(i, 12, item_figi)
                self.ui.results_table.setItem(i, 13, item_instrument_type)
                self.ui.results_table.setItem(i, 14, item_date)
                self.ui.results_table.setItem(i, 15, item_brocker_name)
                self.ui.results_table.setItem(i, 16, item_operation_type)
                self.ui.results_table.setItem(i, 17, item_trades)
                self.ui.results_table.setItem(i, 18, item_asset_uid)
                self.ui.results_table.setItem(i, 19, item_position_uid)
                self.ui.results_table.setItem(i, 20, item_instrument_uid)
                self.ui.results_table.setItem(i, 21, item_operation_type_enum)

            self.ui.results_table.resizeColumnsToContents()
            self.ui.results_table.hideColumn(0)
            self.ui.results_table.hideColumn(3)
            self.ui.results_table.hideColumn(15)
            self.ui.results_table.hideColumn(17)
            self.ui.results_table.hideColumn(18)
            self.ui.results_table.hideColumn(19)
            self.ui.results_table.hideColumn(20)
            self.ui.results_table.hideColumn(21)
            self.ui.results_table.setHorizontalHeaderLabels(labels_list)
            self.ui.results_table.horizontalHeader().show()
            self.ui.results_table.verticalHeader().show()
            #self.ui.results_table.setVerticalHeader()

    def get_table_type(self):
        '''Возвращает тип журнала (локальный или брокера) в сформированной таблице
        '''
        row = self.ui.results_table.currentRow()
        column_count = self.ui.results_table.columnCount()

        data = []
        for col in range(column_count):
            data.append(self.ui.results_table.item(row,col).text())
        # log.debug(f'{__name__} -> data {data}')
        if data[0] == "local_log":
            # log.debug(f'{__name__} -> Is_local_log {data[0]=="local_log"}')
            pass
        if data[0] == "brocker_log":
            # log.debug(f'{__name__} -> Is_local_log {data[0]=="local_log"}')
            pass
        return data[0]

    def mark_row(self):
        '''Выделение строки цветом
        '''
        #log.debug(f'{__name__} -> mark_row() running!!!')
        row_id = self.ui.results_table.currentRow()
        column_count = self.ui.results_table.columnCount()
        #Перекрасим выбранную строку
        for col_id in range(column_count):
            item = self.ui.results_table.item(row_id,col_id)
            item.setBackground(QColor(188,143,143))

    """Описание слотов. Начало.
    """

    def resize_function(self):
        '''Функция возвращает действие для сигнала изменения размера окна
        '''
        # Возвращает ширину и высоту элемента
        get_w_h = lambda object: (object.geometry().getRect()[2], 
                                  object.geometry().getRect()[3])
        history_w_width, history_w_height = get_w_h(self)
        # Необходио передать начальные размеры главному виджету так как в инициализации окна имеется сигнал
        # resize который не может быть вызван без изменения размера окна
        self.ui.general_widget.resize(history_w_width-10, history_w_height-15)
        # Исходные размеры элементов окна
        general_widget_width, general_widget_height = get_w_h(self.ui.general_widget)
        position_table_width, position_table_height = get_w_h(self.ui.results_table)


        #self.ui.general_widget.resize(general_widget_width, general_widget_height+1)
        self.ui.results_table.resize(general_widget_width-20, general_widget_height-190)



    def edit_transaction_from_local_db(self):
        '''Метод получения данных из таблицы results_table
        и подстановка данных в форму для редактирования данных в локаной БД'''
        row = self.ui.results_table.currentRow()
        column_count = self.ui.results_table.columnCount()

        data = list()
        for col in range(column_count):
            data.append(self.ui.results_table.item(row,col).text())
        # log.debug(f'{__name__} -> data {data}')

        sender = self.sender()
        new_window=TransactionWindow()
        #Передаем в объект окна название кнопки для заголовка
        new_window.set_title(f'{sender.text()} запись id {data[1]}')
        new_window.setModal(False)
        if data[0] == "local_log":
            # log.debug(f'{__name__} -> Is_local_log {data[0] == "local_log"}')
            new_window.ui.Transactio_type.setEditable(True)
            new_window.ui.Transactio_type.setEditText(data[3])
            new_window.ui.Brocker.setEditable(True)
            new_window.ui.Brocker.setEditText(data[4])
            new_window.ui.Brocker_account.setEditable(True)
            new_window.ui.Brocker_account.setEditText(data[5])
            new_window.ui.ticker_edit.setText(data[6])
            new_window.ui.instrument_name.setText(data[7])
            new_window.ui.Currency.setText(data[8])
            new_window.ui.price_edit.setText(data[9])
            new_window.ui.volume_edit.setText(data[11])
            new_window.ui.fee_edit.setText(data[12])
            new_window.ui.nkd_edit.setText(data[10])
            new_window.ui.description.setText(data[13])
            qdate = QDate.fromString(data[2][:10],"yyyy-MM-dd")
            str_time = data[2][11:]
            qtime = QTime.fromString(str_time,"HH:mm:ss")
            new_window.ui.dateTimeEdit.setDate(qdate)
            new_window.ui.dateTimeEdit.setTime(qtime)
        new_window.ui.label.setScaledContents(True)
        new_window.ui.label.setText(f"Редактировать сведения об операции id {data[1]}")
        new_window.exec()

    def edit_transaction_with_safe_new_one(self):
        '''Метод получения данных из таблицы results_table
        и подстановка данных в форму для сохранения новой транзакции
        '''
        row_id = self.ui.results_table.currentRow()
        column_count = self.ui.results_table.columnCount()

        #Получим данные из выбранной строки
        data = list()
        for col_id in range(column_count):
            try:
                data.append(self.ui.results_table.item(row_id,col_id).text())
            except:
                # log.error(f'Ошибка получения данных из таблицы', exc_info = True)
                data.append(None)
        #Изменим фон выбранной строки
        self.mark_row()

        # log.debug(f'{__name__} -> edit_transaction_with_safe_new_one -> data {data}')

        sender = self.sender()
        add_new_transaction_window = TransactionWindowEdit()
        #Передаем в объект окна название кнопки для заголовка
        add_new_transaction_window.setWindowTitle(sender.text())
        add_new_transaction_window.setModal(True)

        if data[21]=='22':
            add_new_transaction_window.ui.transaction_type.setText("Sell")
        elif data[21]=='15':
            add_new_transaction_window.ui.transaction_type.setText("Buy")
        add_new_transaction_window.ui.brocker_name.setText(data[15])
        add_new_transaction_window.ui.account_name.setText(data[2])

        instrument_name, instrument_ticker,currency=add_new_transaction_window.get_instrument_attributes(data[12])
        add_new_transaction_window.ui.instrument_name.setText(instrument_name)
        add_new_transaction_window.ui.ticker_edit.setText(instrument_ticker)
        add_new_transaction_window.ui.Currency.setText(currency)
        add_new_transaction_window.ui.price_edit.setText(data[7])
        add_new_transaction_window.ui.volume_edit.setText(data[10])
        str_date = data[14][:10]
        qdate = QDate.fromString(str_date,"yyyy-MM-dd")
        str_time = data[14][11:19]
        qtime = QTime.fromString(str_time,"HH:mm:ss")
        add_new_transaction_window.ui.dateTimeEdit.setDate(qdate)
        add_new_transaction_window.ui.dateTimeEdit.setTime(qtime)
        #Поиск значения НКД для операций с облигациями
        # log.debug(f'{__name__} -> Тип инструмента(data[13]): {data[13]}')
        if data[13].lower()=='bond':
            price = float(data[7])
            quantity = float(data[10])
            payment = float(data[8])
            # log.debug(f'{__name__} -> price, quantity, payment  {price, quantity, payment}')
            nkd_value = (-1)*(payment/quantity)-price
            # log.debug(f'{__name__} -> nkd_value {nkd_value}')
            add_new_transaction_window.ui.nkd_edit.setText(str(round(nkd_value,2)))

        #Поиск значения суммы комисии за оперцию
        operation_id = data[4]
        row_count = self.ui.results_table.rowCount()
        #Поиск номера строки в котором находится значение комиссии
        for row in range(row_count):
            parent_id = self.ui.results_table.item(row, 5)
            parent_id = parent_id.text()
            if operation_id==parent_id:
                fee_row = row
                break
        #log.debug(f'{__name__} -> edit_transaction_with_safe_new_one -> parent_id: {parent_id}')
        #Обработка значения комиссии из таблицы
        #Попытка передать значения комиссии в форму
        try:
            fee = self.ui.results_table.item(fee_row, 8)
            fee = fee.text()
            fee = round(float(fee),2)
            add_new_transaction_window.ui.fee_edit.setText(str((-1)*fee))
        except:
            # log.debug(f'{__name__} edit_transaction_with_safe_new_one -> Значение fee извлечь не удалось')
            add_new_transaction_window.ui.fee_edit.setText(str(0))

        #Показать форму транзакции
        add_new_transaction_window.ui.label.setText(f"Добавить сведения об операции id {operation_id}")
        add_new_transaction_window.exec()

    def create_operation_info_table(self):
        #Очистим таблицу если она была построена ранее
        self.ui.results_table.clear()
        #Получить даты для запроса
        start_date = self.ui.start_date.date()
        start_date = str(start_date.toPython())
        end_date = self.ui.end_date.date()
        end_date = str(end_date.toPython())
        account_list = self.get_account_id_list()
        self.get_brocker_log(account_list, start_date, end_date)


    def create_invest_log_table_v2(self):
        '''Формирует таблицу по данным полученным из локальной БД
        '''
        #Очистим таблицу если она была построена ранее
        self.ui.results_table.clear()
        #Получить даты для запроса
        start_date = self.ui.start_date.date()
        start_date = str(start_date.toPython())
        end_date = self.ui.end_date.date()
        end_date = str(end_date.toPython())
        ticker = self.ui.ticker_edit.text()
        brocker_account = self.ui.Brocker_account.currentText()

        # !!!join_tables строгое соответсвие порядка списка столбцов
        # в переменной "target" и парметров таблиц и столбцов
        # в переменной "source"
        cols_list = ['transactions.transaction_id',
                     "date_time","brocker","brocker_account",
                     "accounts.account_name","transactions.ticker",
                     "instruments.ticker_name", "transaction_type",
                     "transactions.currency","price","volume","fee",
                     "memo", "nkd"]

        join_tables = {"target":["brocker_account","ticker_guid"],
                       "source":{"accounts":["account_id"],
                       "instruments":["id"]}
                       }

        #log.debug(f'{__name__} -> create_invest_log_table_v2 -> из поля self.ui.ticker_edit получен текст: {ticker}')

        #Создадим фильтр
        filter = {'transactions.ticker':ticker,
                  'accounts.account_name':brocker_account,
                  'date_time<':f'{end_date} 23:59:59',
                  'date_time>':f'{start_date} 00:00:00'}


        #Удалим из запроса пустые фильтры
        pop_filter_list = list()
        for key in filter.keys():
            if filter[key] == '':
                pop_filter_list.append(key)

        for key in pop_filter_list:
            filter.pop(key, None)

        #Если выбран переключатель периода "Все", то необходимо удалить фильтр
        #из списка ключей
        if filter['accounts.account_name'] == 'Все':
             filter.pop('accounts.account_name')

        #Если выбран пункт "Все" из списка аккаунтов, то необходимо удалить фильтр
        #из списка ключей
        if self.ui.all_operations.isChecked():
            #log.debug(f'{__name__} -> create_invest_log_table_v2 -> self.ui.all_operations.isChecked() = {self.ui.all_operations.isChecked()}')
            filter.pop('date_time<')
            filter.pop('date_time>')

        # log.debug(f'{__name__} -> create_invest_log_table_v2 -> filter = {str(filter)}')

        #Создаем запрос к БД
        sql_query = ScriptNormalizer("transactions").select(cols_list=cols_list,
                                                              JOIN=join_tables,
                                                              WHERE=filter)


        # log.debug(f'{__name__} -> {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)

        #Создаем таблицу
        if len(data) == 0:
            self.ui.results_table.clear()
            self.ui.results_table.setRowCount(1)
            self.ui.results_table.setColumnCount(1)
            item_message = QTableWidgetItem('В архиве нет данных')
            self.ui.results_table.setItem(0, 0, item_message)
            self.ui.results_table.horizontalHeader().hide()
            self.ui.results_table.verticalHeader().hide()
            self.ui.results_table.setShowGrid(False)

        else:
            self.ui.results_table.clear()
            self.ui.results_table.setRowCount(len(data))
            self.ui.results_table.setColumnCount(len(data[0])+1)
            labels_list=["table",
                         "id",
                         "Дата",
                         "Тип",
                         "Брокер",
                         "Счет",
                         "Тикер",
                         "Название",
                         "Валюта",
                         "Цена",
                         "НКД",
                         "Количество",
                         "Комиссия",
                         "Примечание",
                         "Номер счета"]

            self.ui.results_table.setVerticalHeader(None)
            for i, (id,mydate,brocker,brocker_account,acc_name,ticker,instrument_name,
                    transaction_type,currensy,price,qty,fee,memo,nkd) in enumerate(data):

                if nkd==None:
                    nkd = ''

                item_table = QTableWidgetItem("local_log")
                item_acc_name = QTableWidgetItem(acc_name)
                item_instrument_name = QTableWidgetItem(instrument_name)
                item_id = QTableWidgetItem(str(id))
                item_date = QTableWidgetItem(str(mydate))
                item_transaction_type = QTableWidgetItem(transaction_type)
                item_brocker = QTableWidgetItem(brocker)
                item_brocker_account = QTableWidgetItem(brocker_account)
                item_ticker= QTableWidgetItem(ticker)
                item_currensy = QTableWidgetItem(currensy)
                item_price = QTableWidgetItem(str(price))
                item_qty = QTableWidgetItem(str(qty))
                item_fee = QTableWidgetItem(str(fee))
                item_memo = QTableWidgetItem(memo)
                item_nkd = QTableWidgetItem(str(nkd))

                self.ui.results_table.setItem(i, 0, item_table)
                self.ui.results_table.setItem(i, 1, item_id)
                self.ui.results_table.setItem(i, 2, item_date)
                self.ui.results_table.setItem(i, 3, item_transaction_type)
                self.ui.results_table.setItem(i, 4, item_brocker)
                self.ui.results_table.setItem(i, 5, item_acc_name)
                self.ui.results_table.setItem(i, 6, item_ticker)
                self.ui.results_table.setItem(i, 7, item_instrument_name)
                self.ui.results_table.setItem(i, 8, item_currensy)
                self.ui.results_table.setItem(i, 9, item_price)
                self.ui.results_table.setItem(i, 10, item_nkd)
                self.ui.results_table.setItem(i, 11, item_qty)
                self.ui.results_table.setItem(i, 12, item_fee)
                self.ui.results_table.setItem(i, 13, item_memo)
                self.ui.results_table.setItem(i, 14, item_brocker_account)

                self.ui.results_table.hideColumn(0)
                self.ui.results_table.hideColumn(1)
                self.ui.results_table.hideColumn(14)
            self.ui.results_table.setHorizontalHeaderLabels(labels_list)
            #self.ui.results_table.resizeRowsToContents()
        self.ui.results_table.resizeColumnsToContents()

    def open_transaction_form(self):
        '''Описание окна формы записи
        '''
        sender = self.sender()
        new_window=TransactionWindow()
        new_window.set_title(sender.text())    #Передаем в объект окна название кнопки для заголовка
        new_window.setModal(False)
        new_window.ui.label.setText(f"Добавить сведения об операции")
        new_window.exec()

    def the_button_was_clicked(self):
        '''Описывает стандартную кнопку
        '''
        sender = self.sender()
        # log.debug(f'btn "{sender.text()}" Clicked!')

    def the_button_was_toggled(self, checked):
        '''Кнопка переключатель.
        Аргумент "checked" отражает состояние кнопки: True или False
        '''
        sender = self.sender()
        # log.debug(f'btn "{sender.text()}" Checked?, {checked}')

    '''Описание слотов. Конец.'''
