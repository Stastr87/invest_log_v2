#Standart module import
# from turtle import position
from locale import currency
import config
import sys
import re
import os
import platform
import shelve
from datetime import datetime
from datetime import timedelta

#UI import section
import matplotlib as mpl
mpl.use('QtAgg')
import matplotlib.pyplot as plt
#from PyQt6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QAction, QCursor
from PySide6.QtCore import QTimer, QDate, Qt, Signal
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QTableWidgetItem,
                               QMenu,
                               QVBoxLayout,
                               QDateTimeEdit)
from ui.ui_main_window import Ui_MainWindow
from history_window import HistoryWindow
from test_panel import TestPanel_Window
from instrument_card_window import BondInstrumentCardWindow, ShareInstrumentCardWindow, EtfInstrumentCardWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#Services import

from services.quotes_service.quotes_servise import MarketDataService
from services.instruments_service.instruments_service import InstrumentsService
from db_integration import DBIntegration
from sql_lib.script_normalizer import ScriptNormalizer
from services.data_converter import DataConverter
from data_processing.data_processing_lib import DataProcessing
import temp_data_util

import config
logger_config = config.get_logger_config()
if 'wind' in platform.system():
    logger_path = logger_config['path']
else:
    logger_path = logger_config['alternative_path']
main_log_file = logger_config['main_window']['name']
file_mode = logger_config['main_window']['mode']
logger_level = logger_config['main_window']['level']

import logging
# Настройка логирования
log_main = logging.getLogger(__name__)
if logger_level.lower() == 'debug':
    log_main.setLevel(logging.DEBUG)
if logger_level.lower() == 'error':
    log_main.setLevel(logging.ERROR)
if logger_level.lower() == 'info':
    log_main.setLevel(logging.INFO)
if logger_level.lower() == 'warning':
    log_main.setLevel(logging.WARNING)
if logger_level.lower() == 'critical':
    log_main.setLevel(logging.CRITICAL)
if logger_level == None:
    log_main.setLevel(logging.NOTSET)
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)
fh = logging.FileHandler(filename=os.path.join(logger_path, main_log_file), mode=file_mode, encoding='utf-8')
fh.setFormatter(formatter)
log_main.handlers.clear()
log_main.addHandler(sh)
log_main.addHandler(fh)

converter = DataConverter()

class InvestLog_v2(QMainWindow):

    resized = Signal()
    def __init__(self, parent=None):


        # Для того что бы правильно проинициализировались элементы окна
        # создаются временные директории
        path = config.get_config()["temp_file"]
        self.temp_file = os.path.abspath(os.path.join(*path))
        if not os.path.exists(self.temp_file):
            os.makedirs(self.temp_file)

        #Важная строка для отслеживания изменения размера окна
        super(InvestLog_v2, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectUi()

        #Отслеживание сигналов изменения размера
        self.resized.connect(self.resize_function)

        log_main.info(f'[{__name__}] InvestLog_v2 main_window is initialized...')

    def connectUi(self):
        #Изменить имя окна
        self.setWindowTitle("Сводные данные активов")
        #Сформировать интерфейс
        self.ui.open_table_view.triggered.connect(self.open_table_view)
        self.ui.open_test_panel.triggered.connect(self.open_test_panel)
        #Применим стиль в этом месте кода для того что бы он правильно редактировался если потребуется
        #Если стиль наследовать из self.ui.setupUi(self) то динамически он менятся криво
        self.ui.positions_table.setStyleSheet(u"QTableView{background-color:rgb(220,220,220);\n"
                                              u"border: 2px solid;\n"
                                              u"border-radius: 7px;\n"
                                              u"border-color: rgb(205, 205, 205);}")
        self.ui.accounts_table.setStyleSheet(u"QTableView{background-color:rgb(220,220,220);\n"
                                             u"border: 2px solid;\n"
                                             u"border-radius: 7px;\n"
                                             u"border-color: rgb(205, 205, 205);}")
        #self.ui.general_widget.setSizePolicy(u"QSizePolicy")
        #Данные из локальной БД для отображения в интерфейсе
        self.instruments_data_list = self.get_instruments()
        self.accounts_data_list = self.get_accounts()
        #Создать контекстное меню
        self.context_menu  =  QMenu(self)
        action1  =  self.context_menu.addAction("Action 1")
        action2  =  self.context_menu.addAction("Action 2")
        action3  =  self.context_menu.addAction(f"Подробности...")

        #Наполним интерфейс данными сразу после запуска
        self.update_positions_info()
        self.update_quotes()
        self.update_total_label()

        #Далее интерфес будет обновляться по таймеру
        #Вывод информации по бумагам на всех счетах из временного файла
        update_positions_timer = QTimer(self)
        update_positions_timer.timeout.connect(self.update_positions_info)
        update_positions_timer.start(60000)

        #Обновление которовок по списку бумаг
        update_quotes_timer = QTimer(self)
        update_quotes_timer.timeout.connect(self.update_quotes)
        update_quotes_timer.timeout.connect(self.update_total_label)
        update_quotes_timer.start(60000)



        """Описание сигналов для элементов интерфейса.
        Начало
        """


        #Действие выбора ячейки в таблице
        self.ui.positions_table.cellClicked.connect(self.get_select_item)

        #Действия в контекстном меню
        action1.triggered.connect(self.action1_triggered)
        action2.triggered.connect(self.action2_triggered)
        action3.triggered.connect(self.action3_triggered)

        """Описание сигналов для элементов интерфейса.
        Конец
        """

    def contextMenuEvent(self, event):
        # Show the context menu
        self.context_menu.exec(event.globalPos())

    def action1_triggered(self):
        # Handle the "Action 1" action
        pass

    def action2_triggered(self):
        # Handle the "Action 2" action
        pass

    def action3_triggered(self, action):
        # Handle the "Action 3" action
        self.open_instrument_card()
        pass

    def get_selected_instrument_name(self):
        '''Возвращает имя инструмента в активной ячейке
        '''
        row = self.ui.positions_table.currentRow()
        if row == -1:
            instrument_name = self.ui.positions_table.item(1,1).text()
        else:
            instrument_name = self.ui.positions_table.item(row,1).text()
        log_main.debug(f'{__name__} -> get_selected_instrument_name() -> instrument_name: {instrument_name}')
        return instrument_name

    def get_accounts(self):
        '''Возвращает из локальной БД
        список словарей вида {"account_id":"account_name"}
        '''
        #Столбцы выборки
        cols_list = ["account_id","account_name"]
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("accounts").select(cols_list = cols_list)
        #log.debug(f'{__name__} -> get_accounts() -> sql_query: {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        accounts_data_list = []
        for item in data:
            account_id, account_name = item
            account_data = {account_id:account_name}
            accounts_data_list.append(account_data)
        return accounts_data_list

    def get_instruments(self):
        '''Возвращает из локальной БД
        список кортежей вида (figi, ticker_name, instrument_type)
        '''
        #Столбцы выборки
        cols_list = ["figi","ticker_name","instrument_type","currency", "ticker"]
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("instruments").select(cols_list = cols_list)
        log_main.debug(f'[{__name__}] get_instruments() -> sql_query: {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        return data

    def resizeEvent(self, event):
            '''Действие при изменении размера окна

            DOC: https://doc.qt.io/qtforpython-6/overviews/signalsandslots.html#signals-slots
            '''
            self.resized.emit()
            return super(InvestLog_v2, self).resizeEvent(event)
    """Описание слотов. Начало
    """
    def open_table_view(self):
        self.new_window = HistoryWindow()
        self.new_window.show()

    def open_test_panel(self):
        self.new_window = TestPanel_Window()
        self.new_window.show()

    def open_instrument_card(self):
        row = self.ui.positions_table.currentRow()
        figi_data = self.ui.positions_table.item(row,0).text()
        #log.debug(f'{__name__} -> open_instrument_card() -> figi_data: {figi_data}')
        istrument_type = self.ui.positions_table.item(row,2).text()
        instrument_name = self.ui.positions_table.item(row,1).text()
        instrument_ticker = self.ui.positions_table.item(row,6).text()

        if istrument_type == 'Bond':
            #Наполнеине интерфейса карточки облигации информацией
            #Получение данных
            instruments_request = InstrumentsService()
            bond_info = instruments_request.get_bond_by_figi(figi_data)
            nkd = bond_info.instrument.aci_value
            nkd = converter.tink_money_value_to_float(nkd)
            currency = bond_info.instrument.currency
            if currency.lower() == 'rub':
                currency = 'Руб.'
            perpetual_flag = bond_info.instrument.perpetual_flag
            maturity_date = bond_info.instrument.maturity_date
            nominal = bond_info.instrument.nominal
            nominal = converter.tink_money_value_to_float(nominal)
            log_main.debug(f'[{__name__}] -> [open_instrument_card()] -> maturity_date: {maturity_date.strftime("%B %d, %Y")} \n type(maturity_date): {type(maturity_date)}')
            price = float(self.ui.positions_table.item(row,4).text())
            qty = self.get_instrument_qty(row)
            total_price = round(price*qty)
            description_text = self.get_instrument_description_from_local_db(figi_data)
            #Цена всех активов
            all_assets_price = self.get_all_assets_price()
            #Вес инструмента в портфеле
            weight = (total_price/all_assets_price)*100
            #Сведения о купоне облигации
            nearest_coupon_date, nearest_coupon_value = instruments_request.get_nearest_coupon(figi_data)
            #Данные для графика
            end_time_request = datetime.now()
            delta = timedelta(days=365)
            start_time_request = end_time_request - delta
            #Соберем данные для построения графика в кортеж
            data = (figi_data, start_time_request, end_time_request, instrument_ticker, nominal)

            #Создать объект нового окна
            self.new_window  =  BondInstrumentCardWindow(data, currency)

            #Формирование интерфейса
            self.new_window.setWindowTitle(f'Подробности {instrument_name}')
            self.new_window.setModal(False)
            self.new_window.ui.bond_instrument_card_label.setText(instrument_name)
            self.new_window.ui.Instrument_price.setText(f'{price} {currency}')
            self.new_window.ui.instrument_quantity.setText(f'{qty} шт.')
            self.new_window.ui.total_price.setText(f'{round(total_price, 2)} {currency}')
            self.new_window.ui.description.setText(description_text)
            self.new_window.ui.figi_label.setText(figi_data)
            self.new_window.ui.bond_nkd.setText(f'{round(nkd,2)} {currency}')
            self.new_window.ui.weight_value.setText(f'{round(weight,2)} %')
            if perpetual_flag == True:
                self.new_window.ui.maturity_date_label.setText(f'Дата колл-опциона')
                self.new_window.ui.maturity_date.setText(f'Бессрочная')
            if perpetual_flag == False:
                self.new_window.ui.maturity_date.setText(f'{maturity_date.strftime("%d.%m.%Y")}')
            self.new_window.ui.coupon_date.setText(f'{nearest_coupon_date.strftime("%d.%m.%Y")}')
            self.new_window.ui.coupon.setText(f'{converter.tink_money_value_to_float(nearest_coupon_value)} {currency}')
            qdate_start = QDate(start_time_request.year, start_time_request.month, start_time_request.day)
            self.new_window.ui.start_date.setDate(qdate_start)
            qdate_end = QDate(end_time_request.year, end_time_request.month, end_time_request.day)
            self.new_window.ui.end_date.setDate(qdate_end)

        if istrument_type == 'Stock':
            #Наполнеине интерфейса карточки акции информацией
            #Данные для формирования информационного наполнения окна
            price = float(self.ui.positions_table.item(row,4).text())
            qty = self.get_instrument_qty(row)
            total_price = round(price*qty,2)
            #figi = self.ui.positions_table.item(row,0).text()
            description_text = self.get_instrument_description_from_local_db(figi_data)
            all_assets_price = self.get_all_assets_price()
            weight = (total_price/all_assets_price)*100
            #log.debug(f'{__name__} -> open ShareInstrumentCardWindow() -> {instrument_name} price: {price} qty: {qty} total_price: {total_price}')
            instruments_request = InstrumentsService()
            share_info = instruments_request.get_instrument_by(figi_data)
            currency = share_info.instrument.currency
            if currency.lower() == 'rub':
                currency = 'Руб.'
            #ДАнные для формирования графика
            end_time_request = datetime.now()
            delta = timedelta(days=365)
            start_time_request = end_time_request - delta
            #Соберем данные для построения графика в кортеж
            data = (figi_data, start_time_request, end_time_request, instrument_ticker)

            #Создать объект нового окна
            self.new_window = ShareInstrumentCardWindow(data, currency)

            #Заполнеине интерфейса данными
            self.new_window.setWindowTitle(f'Подробности {instrument_name}')
            self.new_window.setModal(False)
            self.new_window.ui.share_instrument_card_label.setText(instrument_name)
            self.new_window.ui.Instrument_price.setText(f'{price} {currency}')
            self.new_window.ui.instrument_quantity.setText(f'{qty} шт.')
            self.new_window.ui.total_price.setText(f'{round(total_price, 2)} {currency}')
            self.new_window.ui.description.setText(description_text)
            self.new_window.ui.figi_label.setText(figi_data)
            self.new_window.ui.weight_value.setText(f'{round(weight,2)} %')
            qdate_start = QDate(start_time_request.year, start_time_request.month, start_time_request.day)
            self.new_window.ui.start_date.setDate(qdate_start)
            qdate_end = QDate(end_time_request.year, end_time_request.month, end_time_request.day)
            self.new_window.ui.end_date.setDate(qdate_end)

        if istrument_type == 'Etf':
            #Наполнеине интерфейса карточки фонда информацией
            #Получение данных
            #figi=self.ui.positions_table.item(row,0).text()
            price = float(self.ui.positions_table.item(row,4).text())
            qty = self.get_instrument_qty(row)
            total_price = price*qty
            description_text=self.get_instrument_description_from_local_db(figi_data)
            #Цена всех активов
            all_assets_price=self.get_all_assets_price()
            #Вес инструмента в портфеле
            weight=(total_price/all_assets_price)*100
            instruments_request = InstrumentsService()
            etf_info = instruments_request.get_instrument_by(figi_data)
            currency = etf_info.instrument.currency
            if currency.lower() == 'rub':
                currency = 'Руб.'

            #Данные для построения графика
            end_time_request = datetime.now()
            delta = timedelta(days=365)
            start_time_request = end_time_request - delta
            #Соберем данные для построения графика в кортеж
            data = (figi_data, start_time_request, end_time_request, instrument_ticker)
            # Создать объект нового окна
            self.new_window  = EtfInstrumentCardWindow(data, currency)

            #Формирование интерфейса
            self.new_window.setWindowTitle(f'Подробности {instrument_name}')
            self.new_window.setModal(False)
            self.new_window.ui.etf_instrument_card_label.setText(instrument_name)
            self.new_window.ui.Instrument_price.setText(f'{price} {currency}')
            self.new_window.ui.instrument_quantity.setText(f'{qty} шт.')
            self.new_window.ui.total_price.setText(f'{round(total_price, 2)} {currency}')
            self.new_window.ui.description.setText(description_text)
            self.new_window.ui.figi_label.setText(figi_data)
            self.new_window.ui.weight_value.setText(f'{round(weight,2)} %')
            qdate_start = QDate(start_time_request.year, start_time_request.month, start_time_request.day)
            self.new_window.ui.start_date.setDate(qdate_start)
            qdate_end = QDate(end_time_request.year, end_time_request.month, end_time_request.day)
            self.new_window.ui.end_date.setDate(qdate_end)

        self.new_window.show()

    def get_instrument_description_from_local_db(self,figi):
        '''Получение данных об инструменте из локальной БД

        Примечание: Возможно имеет смысл перенести в отдельный модуль...
        '''
        cols_list=['instrument_memo']
        filter={'instruments.figi':str(f"{figi}")}
        sql_query=ScriptNormalizer("instruments").select(cols_list=cols_list,
                                                              WHERE=filter)
        log_main.debug(f'[{__name__}] get_instrument_description_from_local_db() -> sql_query: \n{sql_query}')
        #Создание подключения к БД
        db_connection=DBIntegration()
        #Отправка запроса
        data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        instrument_description=data[0][0]
        log_main.debug(f'[{__name__}] get_instrument_description_from_local_db() -> instrument_description: {instrument_description}')
        return instrument_description

    def get_currency_price_list(self):
        '''Загружает из временного файла актуальные курсы валют
        '''
        shelveFile = shelve.open(self.temp_file)
        currency_price_list = shelveFile['currencies']
        return currency_price_list

    def get_currency_price(self, currency_id):
        '''Функция возвращает текущую цену валюты
        '''
        #Переписать Функция так что бы дынные возвращались из временного файла
        currency_list_request = InstrumentsService()
        currency_list = currency_list_request.get_currencies()

        currency_list
        currency_figi = None
        for currency in currency_list.instruments:
            if currency.iso_currency_name == currency_id.lower():
                currency_figi = currency.figi
                break

        currency_price_list = self.get_currency_price_list()
        currency_price = None
        for price in currency_price_list:
            if currency_figi == price["figi"]:
                currency_price = price["price"]
        return currency_price

    def get_last_prices_list(self,figi_list):
        '''
        '''
        # Ф-ия set()-преобразование списка в множество, а затем ф-ия list(),
        # обратно в список с целью устранить дубликаты.
        # Множества не могут содержать одинаковые элементы.
        normalized_figi_list  =  list(set(figi_list))
        body = {"figi_list":normalized_figi_list}
        request = MarketDataService(BODY = body)
        response_data, error_massage = request.get_quotes_by_figi()
        # Добавить обработчик ошибок на случай:
        # *Нет связи с сервером
        # *Не авторизован
        if error_massage == "I'm fine":
            last_prices_list = response_data.last_prices
        else:
            last_prices_list = response_data
            log_main.error(f'[{__name__}] get_last_prices_list() -> error_massage:{error_massage}')
        return last_prices_list

    def update_quotes(self):
        ''' ПЕРЕНЕСТИ В data_updater.py
        Функция дополняет таблицу self.ui.positions_table
        в главном окне:
        столбец 4 - актуальная котировка инструмента
        '''
        _, positions_storage = temp_data_util.get_stored_data(self.temp_file)
        positions_info = positions_storage['positions_info']

        positions_list = temp_data_util.get_normalized_positions_list(positions_info)
        currencies_list = temp_data_util.get_currencies_positions_list(positions_info)

        main_window_positions_list = positions_list + currencies_list

        log_main.debug(f'[{__name__}] update_quotes() -> main_window_positions_list:{main_window_positions_list}')

        #Составим список инструментов на всех счетах удалив дубликаты
        #Этот список будет использован для запроса котировок
        figi_list = list(map(lambda main_window_position: main_window_position['figi'],
                             main_window_positions_list))

        last_prices_list = self.get_last_prices_list(figi_list)
        last_price_json_list = []
        for item in last_prices_list:
            item_price = converter.tink_quotation_to_float(item.price)
            last_price_json_item = {"figi":item.figi,
                                    "price":item_price}
            last_price_json_list.append(last_price_json_item)

        row_amount = self.ui.positions_table.rowCount()

        for quote in last_price_json_list:
            for i in range(row_amount):
                if self.ui.positions_table.item(i, 0).text() == quote["figi"]:
                    price = quote["price"]
                    if quote["price"] == 0:
                        '''Если запрос last_price вернул цену 0,
                        то запросим цену на момент закрытия торгов по инструменту
                        '''
                        request  =  MarketDataService()
                        close_price_response  =  request.get_close_prices_request(quote["figi"])
                        close_price = close_price_response.close_prices
                        # log_main.debug(f'[{__name__}] update_quotes() -> price in last_price_json_list instrument_figi {quote["figi"]}: close_price = {close_price} ')
                        price = converter.tink_quotation_to_float(close_price[0].price)


                    price = round(price,2)

                    try:
                        if self.ui.positions_table.item(i, 2).text() == 'Bond':
                            instrument_request = InstrumentsService()
                            bond_obj = instrument_request.get_bond_by_figi(quote["figi"])
                            bond_nominal = converter.tink_quotation_to_float(bond_obj.instrument.nominal)
                            bond_nkd = converter.tink_quotation_to_float(bond_obj.instrument.aci_value)
                            log_main.debug(f'[{__name__}] update_quotes() -> bond_nominal = {bond_nominal}, bond_nkd = {bond_nkd}')
                            price = bond_nominal*(price/100)+bond_nkd
                            price = round(price,2)
                    except:
                        log_main.error(f'[{__name__}] update_quotes() -> ошибка получения значения из таблицы positions_table', exc_info=True)
                    try:
                        except_currency_list = ['RUB', 'rub']
                        if self.ui.positions_table.item(i, 5).text() not in except_currency_list:
                            currency_table_id = self.ui.positions_table.item(i, 5).text()
                            log_main.debug(f'[{__name__}] update_quotes() -> в таблице позиций найден инструмент {self.ui.positions_table.item(i, 0).text()} в валюте {currency_table_id}')
                            #Получаем актуальную цену валюты из временного файла
                            currency_price = self.get_currency_price(currency_table_id)
                            currency_price = float(currency_price.replace(',','.'))
                            log_main.debug(f'[{__name__}] update_quotes() -> Для подсчета стоимости актива применяется котировка {currency_table_id}/RUB {currency_price}')
                            price = round(price*currency_price,2)
                    except:
                        log_main.error(f'[{__name__}] update_quotes() -> ошибка получения значения из таблицы positions_table', exc_info=True)

                    item_quote  =  QTableWidgetItem(str(price))
                    self.ui.positions_table.setItem(i, 4, item_quote)

        self.ui.positions_table.resizeColumnsToContents()

    def get_instrument_qty(self,row_number):
        ''' Функция возвращает количество бумаг на всех счетах по
        данным из таблицы positions_table
        '''
        try:
            qty = self.ui.positions_table.item(row_number, 3).text()
            search_patern = '[-+]?\\d+'    #патерн поиска любых цифр в строке
            match = re.search(search_patern,qty)
            qty = int(match[0])
        except:
            qty=0
            log_main.error(f'[{__name__}] update_quotes() -> ошибка получения значения из таблицы positions_table', exc_info=True)
        return qty

    def get_all_assets_price(self):
        '''Функция возвращает сумму активов в денежном выражении
        по данным таблицы positions_table
        '''
        row_amount = self.ui.positions_table.rowCount()
        total_money = 0
        for i in range(row_amount):
            qty = self.get_instrument_qty(i)
            try:
                price = self.ui.positions_table.item(i, 4).text()
            except Exception:
                price = 1
                log_main.error('Ошибка получения цены инструмента', exc_info=True)
            price = float(price)

            total_money_by_instrument = qty*price
            total_money = total_money+total_money_by_instrument
        return total_money

    def update_total_label(self):
        '''Функция подсчитывает сумму средств по всем инструментам
        и обновляет self.ui.total_maney_value_label
        '''
        total_money=self.get_all_assets_price()
        self.ui.total_maney_value_label.setText(str(round(total_money,2)))

    def update_positions_info(self):
        '''Функция формирует таблицу self.ui.positions_table
        в главном окне из следующих столбцов:
        столбец 0 - item_figi
        столбец 1 - instrument_name
        столбец 2 - instrument_type
        столбец 3 - total_qty (общее количество бумаг на счетах)
        столбец 4 - значение актуальных котировок
        столбец 5 - валюта инструмента
        столбец 6 - тикер инструмента
        '''

        last_update, positions_storage = temp_data_util.get_stored_data(self.temp_file)
        str_time = last_update.strftime("%d.%m.%Y %H:%M")
        self.ui.last_update_lable.setText(f'Последнее обновление {str_time}')
        positions_info = positions_storage['positions_info']
        positions_list = temp_data_util.get_normalized_positions_list(positions_info)
        currencies_list = temp_data_util.get_currencies_positions_list(positions_info)

        #log_main.debug(f'[{__name__}] update_positions_info() -> currencies_list {currencies_list}')

        main_window_positions_list = positions_list + currencies_list

        #Составим список инструментов на всех счетах удалив дубликаты
        # Этот список будет отображаться в таблице позиций
        figi_list = list(map(lambda main_window_position: main_window_position['figi'],
                             main_window_positions_list))

        # Ф-ия set()-преобразование списка в набор (удаление дубликотов),
        # а затем ф-ия list(), чтобы преобразовать его обратно в список
        normalized_figi_list  =  list(set(figi_list))

        #Отобразим таблицу по списку инструментов на всех счетах
        self.ui.positions_table.setRowCount(len(normalized_figi_list))
        self.ui.positions_table.setColumnCount(7)

        for i in range(len(normalized_figi_list)):
            item_figi  =  QTableWidgetItem(normalized_figi_list[i])
            self.ui.positions_table.setItem(i, 0, item_figi)

            # Отобразим в списке имена инструментов
            # Все гениальное просто keys  =  [*dict] - получить список ключей словаря
            for local_db_instrument_data in self.instruments_data_list:
                figi = local_db_instrument_data[0]
                #Подставляем имя инструмента в таблицу
                if normalized_figi_list[i] == figi:
                    item_instrument_name  =  QTableWidgetItem(local_db_instrument_data[1])
                    self.ui.positions_table.setItem(i, 1, item_instrument_name)
                    item_instrument_type  =  QTableWidgetItem(local_db_instrument_data[2])
                    self.ui.positions_table.setItem(i, 2, item_instrument_type)
                    item_instrument_currency  =  QTableWidgetItem(local_db_instrument_data[3])
                    self.ui.positions_table.setItem(i, 5, item_instrument_currency)
                    #Подсчитаем количество бумаг на всех счетах
                    total_qty = 0
                    for position in main_window_positions_list:
                        if figi == position["figi"]:
                            quantity = position["quantity"]
                            total_qty += quantity

                    #log.debug(f'{__name__} -> update_positions_info() -> total_qty:  {total_qty}')
                    #Подставляем количество бумаг в таблицу
                    item_total_qty  =  QTableWidgetItem(f'    {total_qty} шт.')
                    self.ui.positions_table.setItem(i, 3, item_total_qty)
                    item_instrument_ticker  =  QTableWidgetItem(local_db_instrument_data[4])
                    self.ui.positions_table.setItem(i, 6, item_instrument_ticker)

        self.ui.positions_table.hideColumn(0)
        self.ui.positions_table.hideColumn(2)
        self.ui.positions_table.hideColumn(5)
        self.ui.positions_table.hideColumn(6)
        #self.ui.positions_table.hideColumn(4)
        self.ui.positions_table.horizontalHeader().hide()
        self.ui.positions_table.verticalHeader().hide()
        self.ui.positions_table.setShowGrid(False)

        #Создать контекстное меню
        self.menu = QMenu()
        #Создать действие меню( Имя, Функция)
        #Далее это действие меню должно быть добавлено к каждому елементу таблицы
        self.menu.addAction("Подробности...",self.open_instrument_card)

    def get_select_item(self):
        '''Формирует таблицу accounts_table по сведениям о выбранном элементе в таблице
        positions_table
        столбец 0 - счет
        столбец 1 - имя счета
        столбец 2 - количество бумаг на счете
        столбец 3 - стоимость инструмента на счете
        '''
        row = self.ui.positions_table.currentRow()
        figi_data = self.ui.positions_table.item(row,0).text()
        try:
            price = self.ui.positions_table.item(row,4).text()
        except Exception:
            price = 1
            log_main.error('Ошибка получения цены инструмента', exc_info=True)
        currency  = self.ui.positions_table.item(row,5).text()
        if currency.lower()=='rub':
            currency = 'Руб.'
        log_main.debug(f'[{__name__}] get_select_item() -> figi_data: {figi_data}\n item price')

        _, positions_storage = temp_data_util.get_stored_data(self.temp_file)
        positions_info = positions_storage['positions_info']
        accounts_table_positions_list = temp_data_util.get_normalized_positions_list(positions_info)

        accouts_list = list()
        qty_list = list()
        for item in accounts_table_positions_list:
            if item["figi"] == figi_data:
                accouts_list.append(item["account_id"])
                qty_list.append(item["quantity"])

        self.ui.accounts_table.setRowCount(len(accouts_list))
        self.ui.accounts_table.setColumnCount(4)
        total_account_price_value_list = []
        for i in range(len(accouts_list)):
            account_id = accouts_list[i]
            qty = qty_list[i]
            item_account  =  QTableWidgetItem(account_id)
            self.ui.accounts_table.setItem(i, 0, item_account)
            item_quantity = QTableWidgetItem(f'    {qty} шт.')
            item_quantity.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.ui.accounts_table.setItem(i, 2, item_quantity)

            for local_db_account_data in self.accounts_data_list:
                #Получаем список аккаунтов
                account_id_key_list = [*local_db_account_data]
                #Подставляем имя аккаунта в таблицу
                for item in account_id_key_list:
                    if str(item)  ==  account_id:
                        item_account_name  =  QTableWidgetItem(local_db_account_data[item])
                        self.ui.accounts_table.setItem(i, 1, item_account_name)
                account_total_price = round(qty * float(price),2)
                item_account_total_price = QTableWidgetItem(f'{account_total_price} {currency}')
                item_account_total_price.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.ui.accounts_table.setItem(i, 3, item_account_total_price)
            total_account_price_value_list.append(account_total_price)

        #Добавим еще одну строку
        row_len=self.ui.accounts_table.rowCount()
        self.ui.accounts_table.insertRow(row_len)

        #log.debug(f'{__name__} -> get_select_item () -> row_len: {row_len}')
        empty_item = QTableWidgetItem('-')
        total_account_item  = QTableWidgetItem('Итого:')
        total_account_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        total_qty_item = QTableWidgetItem(f'{sum(qty_list)} шт.')
        total_qty_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        total_price_item = QTableWidgetItem(f'{round(sum(total_account_price_value_list),2)} {currency}')
        self.ui.accounts_table.setItem(row_len, 0, empty_item)
        self.ui.accounts_table.setItem(row_len, 1, total_account_item)
        self.ui.accounts_table.setItem(row_len, 2, total_qty_item)
        self.ui.accounts_table.setItem(row_len, 3, total_price_item)

        self.ui.accounts_table.hideColumn(0)
        self.ui.accounts_table.resizeColumnsToContents()
        self.ui.accounts_table.horizontalHeader().hide()
        self.ui.accounts_table.verticalHeader().hide()
        self.ui.accounts_table.setShowGrid(False)

    def resize_function(self):
        '''Функция возвращает действие для сигнала изменения размера окна
        '''
        # Возвращает ширину и высоту элемента
        get_w_h = lambda object: (object.geometry().getRect()[2], object.geometry().getRect()[3])
        main_w_width, main_w_height = get_w_h(self)
        # Необходио передать начальные размеры главному виджету так как в инициализации окна имеется сигнал
        # resize который не может быть вызван без изменения размера окна
        self.ui.general_widget.resize(main_w_width-10, main_w_height-50)
        # Исходные размеры элементов окна
        general_widget_width, general_widget_height = get_w_h(self.ui.general_widget)
        position_table_width, position_table_height = get_w_h(self.ui.positions_table)
        accounts_table_width, accounts_table_height = get_w_h(self.ui.accounts_table)

        #self.ui.general_widget.resize(general_widget_width, general_widget_height+1)
        self.ui.positions_table.resize(position_table_width, general_widget_height-230)
        self.ui.accounts_table.resize(accounts_table_width, general_widget_height-230)


    '''Описание слотов. Конец
    '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InvestLog_v2()
    window.show()
    sys.exit(app.exec())