import json
import sys
from pprint import pprint
from datetime import datetime
from datetime import timedelta
from sql_lib.script_normalizer import ScriptNormalizer


from PySide6.QtWidgets import (QDialog, QCompleter, QVBoxLayout, QLineEdit, QWidget)
from PySide6 import QtWidgets, QtWebEngineWidgets
from ui.ui_share_instrument_card import Ui_Dialog as Ui_Dialog_Share
from ui.ui_bond_instrument_card import Ui_Dialog as Ui_Dialog_Bond
from ui.ui_etf_instrument_card import Ui_Dialog as Ui_Dialog_Etf
from db_integration import DBIntegration
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from chart_lib.chart import MyChart
import pandas as pd

# import config
# from  my_logger import MyLogger
# logger_config = config.get_logger_config()
# log_file = logger_config['instrument_card_window']
# log = MyLogger(log_file).new_logger

class MyMplCanavas(FigureCanvasQTAgg):
    '''Останется тут как возможный пример рисования графиков в Qt'''
    def __init__(self, fig, parent = None):
        super(MyMplCanavas, self).__init__(fig)


class BondInstrumentCardWindow(QDialog):
    def __init__(self, data, currency):
        '''Инициализация окна инстремента типа Bond
        '''
        super(BondInstrumentCardWindow, self).__init__()
        self.ui = Ui_Dialog_Bond()
        self.ui.setupUi(self)
        self.chart_data = data
        self.y_info = 'Цена, % номинала'
        self.connectUI()
        self.init_chart()

    def connectUI(self):
        '''Описание взаимодействие с кнопками
        '''
        button_save = self.ui.save_button
        button_save.clicked.connect(self.accept)
        button_save.clicked.connect(self.save_data)
        #Сигнал отменить результаты и закрыть окно
        button_cancel = self.ui.cancel_button
        button_cancel.clicked.connect(self.reject)
        #Сигнал для формирования линейного графика
        button_line_chart = self.ui.line_chart_button
        button_line_chart.clicked.connect(self.redraw_line_chart)
        #Сигнал для формирования графика свечей
        button_candle_chart = self.ui.ohlc_button
        button_candle_chart.clicked.connect(self.redraw_candle_chart)

    def init_chart(self):
        '''Формирует график инструмента при загрузки окна
        '''
        chart = MyChart(self.chart_data, self.y_info)
        fig = chart.draw_bond_line_chart()
        self.ui.chart_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def redraw_line_chart(self):
        '''Обновление графика с новыми параметрами из полей окна
        '''

        figi = self.ui.figi_label.text()
        start_date = self.ui.start_date.dateTime().toPython()
        end_date = self.ui.end_date.dateTime().toPython()
        data = (figi, start_date, end_date)
        chart = MyChart(data, self.y_info)
        fig = chart.draw_bond_line_chart()
        self.ui.chart_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def redraw_candle_chart(self):

        figi = self.ui.figi_label.text()
        start_date = self.ui.start_date.dateTime().toPython()
        end_date = self.ui.end_date.dateTime().toPython()
        data = (figi, start_date, end_date)
        chart = MyChart(data, self.y_info)
        fig = chart.draw_candle_chart_v2()
        self.ui.chart_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def save_data(self):
        data={"instrument_memo": self.ui.description.toPlainText()}
        filter={"figi": f"{self.ui.figi_label.text()}"}
        sql_query=ScriptNormalizer("instruments", new_data=data,).update(WHERE=filter)
        db_connection=DBIntegration()
        DBIntegration.script_executer_with_commit(db_connection,sql_query)

class ShareInstrumentCardWindow(QDialog):
    def __init__(self, data, currency):
        '''Инициализация окна подробной информации инструмента типа Share
        '''
        super(ShareInstrumentCardWindow, self).__init__()
        self.ui = Ui_Dialog_Share()
        self.ui.setupUi(self)
        self.chart_data = data
        self.ticker = data[3]
        self.y_info = currency
        self.connectUI()
        self.init_chart()


    def connectUI(self):
        '''Описание взаимодействие с кнопками
        '''
        #Сигнал принять результаты и закрыть окно
        button_save = self.ui.save_button
        #button_save.clicked.connect(self.accept)
        button_save.clicked.connect(self.save_data)
        #Сигнал отменить результаты и закрыть окно
        button_cancel = self.ui.cancel_button
        button_cancel.clicked.connect(self.reject)
        #Сигнал для формирования линейного графика
        button_line_chart = self.ui.line_chart_button
        button_line_chart.clicked.connect(self.redraw_line_chart)
        #Сигнал для формирования графика свечей
        button_candle_chart = self.ui.ohlc_button
        button_candle_chart.clicked.connect(self.redraw_candle_chart)

    def init_chart(self):
        '''Формирует график инструмента при загрузки окна
        '''
        chart = MyChart(self.chart_data, self.y_info)
        fig = chart.draw_line_chart_v2()
        self.ui.chart_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def redraw_line_chart(self):
        '''Обновление графика с новыми параметрами из полей окна
        '''
        figi = self.ui.figi_label.text()
        start_date = self.ui.start_date.dateTime().toPython()
        end_date = self.ui.end_date.dateTime().toPython()
        data = (figi, start_date, end_date, self.ticker)
        chart = MyChart(data, self.y_info)
        fig = chart.draw_line_chart_v2()
        self.ui.chart_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def redraw_candle_chart(self):
        figi = self.ui.figi_label.text()
        start_date = self.ui.start_date.dateTime().toPython()
        end_date = self.ui.end_date.dateTime().toPython()
        data = (figi, start_date, end_date, self.ticker)
        chart = MyChart(data, self.y_info)
        fig = chart.draw_candle_chart_v2()
        self.ui.chart_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def save_data(self):
        data={"instrument_memo": self.ui.description.toPlainText()}
        filter={"figi": f"{self.ui.figi_label.text()}"}
        sql_query=ScriptNormalizer("instruments", new_data=data,).update(WHERE=filter)
        db_connection=DBIntegration()
        DBIntegration.script_executer_with_commit(db_connection,sql_query)

class EtfInstrumentCardWindow(QDialog):
    def __init__(self, data, currency):
        super(EtfInstrumentCardWindow, self).__init__()
        self.ui = Ui_Dialog_Etf()
        self.ui.setupUi(self)
        self.chart_data = data
        self.y_info = currency
        self.init_UI()
        self.connectUI()
        self.init_chart()

    def init_UI(self):
        '''Создает объекты внутри окна
        '''
        #self.browser = QtWebEngineWidgets.QWebEngineView(self)
        #self.ui.chart_widget = QtWidgets.QVBoxLayout(self)
        #self.ui.chart_widget.addWidget(self.browser)

    def connectUI(self):
        '''Описание взаимодействие с кнопками
        '''
        #Сигнал принять результаты и закрыть окно
        button_save = self.ui.Save
        #button_save.clicked.connect(self.accept)
        button_save.clicked.connect(self.save_data)
        #Сигнал отменить результаты и закрыть окно
        button_cancel = self.ui.Cancel
        button_cancel.clicked.connect(self.reject)
        button_line_chart = self.ui.line_chart
        button_line_chart.clicked.connect(self.redraw_line_chart)
        #Сигнал для формирования графика свечей
        button_candle_chart = self.ui.candle_chart
        button_candle_chart.clicked.connect(self.redraw_candle_chart)

    def init_chart(self):
        '''Формирует график инструмента при загрузки окна
        '''
        chart = MyChart(self.chart_data, self.y_info)
        fig = chart.draw_line_chart_v2()
        self.ui.chart_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))




        #log.debug(f'{__name__} -> init_chart() -> type(fig): {type(fig)}')


    def redraw_line_chart(self):
        '''Обновление графика с новыми параметрами из полей окна
        '''
        figi = self.ui.figi_label.text()
        start_date = self.ui.start_date.dateTime().toPython()
        end_date = self.ui.end_date.dateTime().toPython()
        data = (figi, start_date, end_date)
        chart = MyChart(data, self.y_info)
        fig = chart.draw_line_chart_v2()
        self.ui.chart_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def redraw_candle_chart(self):
        figi = self.ui.figi_label.text()
        start_date = self.ui.start_date.dateTime().toPython()
        end_date = self.ui.end_date.dateTime().toPython()
        data = (figi, start_date, end_date)
        chart = MyChart(data, self.y_info)
        fig = chart.draw_candle_chart_v2()
        self.ui.chart_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def save_data(self):
        '''Сохраняет данные введеные в полях окна
        '''
        data={"instrument_memo": self.ui.description.toPlainText()}
        filter={"figi": f"'{self.ui.figi_label.text()}'"}
        sql_query=ScriptNormalizer("instruments", new_data=data,).update(WHERE=filter)
        db_connection=DBIntegration()
        DBIntegration.script_executer_with_commit(db_connection,sql_query)



        """
        '''!!!Останется тут как возможный пример рисования графиков в Qt'''
class EtfInstrumentCardWindow(QDialog):

    def __init__(self, data, currency):
        super(EtfInstrumentCardWindow, self).__init__()
        self.ui = Ui_Dialog_Etf()
        self.ui.setupUi(self)
        self.chart_data = data
        self.y_info = currency
        self.init_UI()
        self.connectUI()
        self.init_chart()

    def init_UI(self):
        '''Создает объекты внутри окна
        '''
        self.canvas = None
        self.chart_box = QVBoxLayout()
        self.ui.chart_widget.setLayout(self.chart_box)

    def connectUI(self):
        '''Описание взаимодействие с кнопками
        '''
        #Сигнал принять результаты и закрыть окно
        button_save = self.ui.Save
        #button_save.clicked.connect(self.accept)
        button_save.clicked.connect(self.save_data)
        #Сигнал отменить результаты и закрыть окно
        button_cancel = self.ui.Cancel
        button_cancel.clicked.connect(self.reject)
        button_line_chart = self.ui.line_chart
        button_line_chart.clicked.connect(self.redraw_line_chart)
        #Сигнал для формирования графика свечей
        button_candle_chart = self.ui.candle_chart
        button_candle_chart.clicked.connect(self.redraw_candle_chart)

    def init_chart(self):
        '''Формирует график инструмента при загрузки окна
        '''
        chart = MyChart(self.chart_data, self.y_info)
        fig = chart.draw_line_chart()
        #log.debug(f'{__name__} -> init_chart() -> type(fig): {type(fig)}')
        if self.canvas:
            self.chart_box.removeWidget(self.canvas)
            self.canvas.deleteLater()
            self.canvas.hide()
        self.canvas = MyMplCanavas(fig)
        self.chart_box.addWidget(self.canvas)

    def redraw_line_chart(self):
        '''Обновление графика с новыми параметрами из полей окна
        '''
        figi = self.ui.figi_label.text()
        start_date = self.ui.start_date.dateTime().toPython()
        end_date = self.ui.end_date.dateTime().toPython()
        data = (figi, start_date, end_date)
        chart = MyChart(data, self.y_info)
        fig = chart.draw_line_chart()
        #log.debug(f'{__name__} -> init_chart() -> type(fig): {type(fig)}')
        if self.canvas:
            self.chart_box.removeWidget(self.canvas)
            self.canvas.deleteLater()
            self.canvas.hide()
        self.canvas = MyMplCanavas(fig)
        self.chart_box.addWidget(self.canvas)

    def redraw_candle_chart(self):
        figi = self.ui.figi_label.text()
        start_date = self.ui.start_date.dateTime().toPython()
        end_date = self.ui.end_date.dateTime().toPython()
        data = (figi, start_date, end_date)
        chart = MyChart(data, self.y_info)
        fig = chart.draw_candle_chart()
        #log.debug(f'{__name__} -> init_chart() -> type(fig): {type(fig)}')
        if self.canvas:
            self.chart_box.removeWidget(self.canvas)
            self.canvas.deleteLater()
            self.canvas.hide()
        self.canvas = MyMplCanavas(fig)
        self.chart_box.addWidget(self.canvas)

    def save_data(self):
        '''Сохраняет данные введеные в полях окна
        '''
        data={"instrument_memo": self.ui.description.toPlainText()}
        filter={"figi": f"'{self.ui.figi_label.text()}'"}
        sql_query=ScriptNormalizer("instruments", new_data=data,).update(WHERE=filter)
        db_connection=DBIntegration()
        DBIntegration.script_executer_with_commit(db_connection,sql_query)
        """