import matplotlib as mpl
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.ticker
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import os
from data_processing.data_processing_lib import DataProcessing
from db_integration import DBIntegration
from sql_lib.script_normalizer import ScriptNormalizer


import temp_data_util
import config

import my_logger
log = my_logger.setup_applevel_logger(file_name = 'chart.log')

class MyChart(object):
    def __init__(self,data,y_info):
        self.data = data
        self.y_info = y_info
        path = config.get_config()["temp_file"]
        self.temp_file = os.path.abspath(os.path.join(*path))
        if not os.path.exists(self.temp_file):
            os.makedirs(self.temp_file)
        log.debug(f'[{__name__}] [MyChart] class is initialized...')

    def draw_bond_line_chart(self):
        '''Возвращает объект линейного графика plotly
        '''
        figi = self.data[0]
        start_date = self.data[1]
        #start_date = self.data[1].toPython()
        end_date = self.data[2]
        #end_date = self.data[2].toPython()
        data = DataProcessing(figi, start_date, end_date)
        raw_data_frame = data.get_local_stored_data()
        close_data_frame = (raw_data_frame[['close']])/100
        #print(f'{__name__} -> draw_line_chart() ->')
        #print(close_data_frame.head(5))
        #print(close_data_frame.tail(5))

        #fig = px.line(close_data_frame)
        fig = px.area(close_data_frame)
        fig.update_yaxes(range=[close_data_frame['close'].min()*0.95,close_data_frame['close'].max()*1.02])
        fig.update_layout(showlegend=False,
                          xaxis_title=None,
                          margin=dict(l=0, r=0, t=0, b=25),
                          yaxis_title=self.y_info,
                          paper_bgcolor='#E0E0E0',
                          #Цвет подложки графика
                          plot_bgcolor='#E0E0E0',
                          #hovermode='y unified',
                          #hoverdistance=-1,
                          hoverlabel=dict(bgcolor='#E0E0E0'))
        fig.update_traces(mode="lines", hovertemplate=None)
        fig.update_layout(hovermode="x")

        #Добавим линии средних цен
        #НЕОБХОДИМО ПЕРЕДАВАТЬ ЗНАЧЕНИЕ НОМИНАЛА ДЛЯ ПОСТРОЕНИЯ ГРАФИКА
        nominal = 1000
        average_buy, average_sell = self.get_average_prices()
        log.debug(f'[{__name__}] -> [draw_bond_line_chart()] -> average_buy, average_sell: {average_buy, average_sell}')
        if average_buy:
            fig.add_hline(y=average_buy/nominal, line_color="green", line_width=1)
        if average_sell:
            fig.add_hline(y=average_sell/nominal, line_color="red", line_width=1)

        return fig

    def draw_line_chart_v2(self):
        '''Возвращает объект линейного графика plotly
        '''
        figi = self.data[0]
        start_date = self.data[1]
        #start_date = self.data[1].toPython()
        end_date = self.data[2]
        #end_date = self.data[2].toPython()
        data = DataProcessing(figi, start_date, end_date)
        raw_data_frame = data.get_local_stored_data()
        close_data_frame = raw_data_frame[['close']]

        #Добавим линии средних цен
        average_buy, average_sell = self.get_average_prices()

        fig = px.area(close_data_frame)
        fig.update_yaxes(range=[close_data_frame['close'].min()*0.95,close_data_frame['close'].max()*1.02])
        fig.update_layout(showlegend=False,
                          xaxis_title=None,
                          margin=dict(l=0, r=0, t=0, b=25),
                          yaxis_title=self.y_info,
                          paper_bgcolor='#E0E0E0',
                          #Цвет подложки графика
                          plot_bgcolor='#E0E0E0',
                          #hovermode='y unified',
                          #hoverdistance=-1,
                          hoverlabel=dict(bgcolor='#E0E0E0'))
        fig.update_traces(mode="lines", hovertemplate=None)
        fig.update_layout(hovermode="x")

        #Добавим линии средних цен
        average_buy, average_sell = self.get_average_prices()
        log.debug(f'[{__name__}] -> [draw_bond_line_chart()] -> average_buy, average_sell: {average_buy, average_sell}')
        if average_buy:
            fig.add_hline(y=average_buy, line_color="green", line_width=1)
        if average_sell:
            fig.add_hline(y=average_sell, line_color="red", line_width=1)
        return fig

    def draw_candle_chart_v2(self):
        '''Возвращает объект plotly.graph_objects графика типа свечи
        '''
        figi = self.data[0]
        start_date = self.data[1]
        end_date = self.data[2]
        log.debug(f'{__name__} -> draw_candle_chart() -> start_date: {start_date}, end_date: {end_date}')
        data = DataProcessing(figi, start_date, end_date)
        raw_data_frame = data.get_local_stored_data()

        fig = go.Figure(data=go.Ohlc(x=raw_data_frame.index,
                    open=raw_data_frame['open'],
                    high=raw_data_frame['high'],
                    low=raw_data_frame['low'],
                    close=raw_data_frame['close']))
        fig.update(layout_xaxis_rangeslider_visible=False)
        fig.update_layout(#autosize=False,
                          #width=700,
                          #height=300,
                          margin=dict(l=10, r=10, t=25, b=10),
                          yaxis_title=f'{self.y_info}',
                          paper_bgcolor='#E0E0E0',
                          #Цвет подложки графика
                          plot_bgcolor='#E0E0E0',
                          #hovermode='y unified',
                          #hoverdistance=-1,
                          hoverlabel=dict(bgcolor='#E0E0E0'))
        return fig

    def draw_line_chart(self):
        '''Возвращает объект линейного графика matplotlib.pyplot
        '''
        figi = self.data[0]
        start_date = self.data[1]
        #start_date = self.data[1].toPython()
        end_date = self.data[2]
        #end_date = self.data[2].toPython()
        data = DataProcessing(figi, start_date, end_date)
        raw_data_frame = data.get_local_stored_data()
        close_data_frame = raw_data_frame[['close']]
        #print(f'{__name__} -> draw_line_chart() ->')
        #print(close_data_frame.head(5))
        #print(close_data_frame.tail(5))

        x = close_data_frame.index
        y = np.array(close_data_frame, dtype=float)


        fig, axes = plt.subplots(nrows=1,
                                 ncols=1,
                                 figsize=(10, 6),
                                 facecolor='#ebebeb', # Цвет в тон виджета
                                                      # на котором размещен график
                                 layout='constrained')

        #Построим линейный график
        axes.plot(x,y,linewidth=1,color = '#084747')

        #Добавим линии средних цен
        average_buy, average_sell = self.get_average_prices()
        log.debug(f'[{__name__}] -> [draw_bond_line_chart()] -> average_buy, average_sell: {average_buy, average_sell}')

        if average_buy:
            axes.axhline(y=average_buy, linestyle='--', linewidth=0.9, color='#005c2b')
        if average_sell:
            axes.axhline(y=average_sell, linestyle='--', linewidth=0.9, color='#b52100')

        #Добавим легенду на график
        legend_patch_list=[]
        if average_buy not in [0,None]:
            average_buy_patch = mpatches.Patch(color='#005c2b',linewidth=0.5, label=f'Средняя покупка {round(average_buy,2)}') #595959
            legend_patch_list.append(average_buy_patch)
        if average_sell not in [0,None]:
            average_sell_patch = mpatches.Patch(color='#b52100',linewidth=0.5, label=f'Средняя продажа {round(average_sell,2)}')
            legend_patch_list.append(average_sell_patch)

        axes.legend(handles=legend_patch_list, facecolor='#cfe2f3',frameon=False)

        #Закрасим область между графиком и осью х
        axes.fill_between(x,
                         y.flatten(), # flatten() - метод для конвертации в
                                      # одноразмерный массив для построения графика
                         y.min()-y.min()*0.1,
                         where=None,
                         interpolate=True,
                         linewidth=1,
                         color = '#0d8282',
                         alpha=0.2)

        #Определение отступов по осям в процентном выражании
        axes.margins(x = 0,
                    y = 0.02,
                    tight = False)
        #Автоматическое масштабирование графика
        axes.autoscale(True,True,True)

        axes.set_facecolor(color='#f5f5f5')
        #fig.suptitle(f'График цены инструмента {figi}')
        axes.set_title(f'{self.y_info}',
                       loc='left',
                       fontstyle='oblique',
                       fontsize='medium',
                       color = '#595959')
        myFmt = mdates.DateFormatter('%m.%y')
        axes.xaxis.set_major_formatter(myFmt)
        axes.xaxis.label.set_color('#595959')
        axes.yaxis.label.set_color('#595959')
        axes.tick_params(colors='#595959', which='both')
        axes.spines['bottom'].set_color('#ebebeb')
        axes.spines['bottom'].set_linewidth(3)
        axes.spines['top'].set_color('#ebebeb')
        axes.spines['top'].set_linewidth(0)
        axes.spines['right'].set_color('#ebebeb')
        axes.spines['left'].set_color('#ebebeb')
        #Автоматическое масштабирование по осям
        axes.autoscale_view(tight=None, scalex=False, scaley=True)
        #Настройки отображения осей
        axes.tick_params()
        plt.xticks(rotation=35, ha='right')
        #Показать координаты последенй точки
        y_text=str(y[-1][0])
        plt.annotate(y_text,
                     xy=(x[-1],y[-1]+5),
                     textcoords='offset fontsize',
                     xytext=(0,0),
                     ha='right')
        return fig

    def draw_line_chart_bond(self):
        '''Возвращает объект линейного графика для облигаций matplotlib.pyplot
        '''
        figi = self.data[0]
        start_date = self.data[1]
        end_date = self.data[2]
        nominal = self.data[4]
        data = DataProcessing(figi, start_date, end_date)
        raw_data_frame = data.get_local_stored_data()
        close_data_frame = raw_data_frame[['close']]

        x = close_data_frame.index
        y = np.array((close_data_frame/100)*nominal, dtype=float)



        #Создадим объект графика
        fig, axes = plt.subplots(nrows=1,
                                 ncols=1,
                                 figsize=(10, 6),
                                 facecolor='#ebebeb', # Цвет в тон виджета
                                                      # на котором размещен график
                                 layout='constrained')

        #Построим линейный график
        axes.plot(x,y,linewidth=1,color = '#084747')

        #Зададим шаг рисок Риски будут следовать с шагом 1.5
        #locator = matplotlib.ticker.MultipleLocator(5)
        #Установим локатор для главных рисок
        #axes.yaxis.set_major_locator(locator)
        average_buy, average_sell = self.get_average_prices()
        try:
            axes.axhline(y=average_buy, linestyle='--', linewidth=0.9, color='#005c2b')
            #axes.text(x[0],average_buy,str(f'{round(average_buy,2)}  '), color='#005c2b', ha="right", va="center")
        except:
            log.error(f'{__name__} -> draw_line_chart_bond() -> Ошибка построения линии средней цены покупки', exc_info=True)
        try:
            axes.axhline(y=average_sell, linestyle='--', linewidth=0.9, color='#b52100')
            #axes.text(x[0],average_sell,str(f'{round(average_sell,2)}  '), color='#b52100', ha="right", va="center")
        except:
            log.error(f'{__name__} -> draw_line_chart_bond() -> Ошибка построения линии средней цены продажи', exc_info=True)

        #Добавим легенду на график
        legend_patch_list=[]
        if average_buy not in [0,None]:
            average_buy_patch = mpatches.Patch(color='#005c2b',linewidth=0.5, label=f'Средняя покупка {round(average_buy,2)}') #595959
            legend_patch_list.append(average_buy_patch)
        if average_sell not in [0,None]:
            average_sell_patch = mpatches.Patch(color='#b52100',linewidth=0.5, label=f'Средняя продажа {round(average_sell,2)}')
            legend_patch_list.append(average_sell_patch)

        axes.legend(handles=legend_patch_list, facecolor='#cfe2f3',frameon=False)

        #Закрасим область между графиком и осью х
        axes.fill_between(x,
                         y.flatten(), # flatten() - метод для конвертации в
                                      # одноразмерный массив для построения графика
                         y.min()-y.min()*0.1,
                         where=None,
                         interpolate=True,
                         linewidth=1,
                         color = '#0d8282',
                         alpha=0.2)
        #Включить сетку на графике
        #plt.grid(True,
        #         color = "grey",
        #         linewidth = '0.7',
        #         axis = "y",
        #         linestyle = '--')

        #Определение отступов по осям в процентном выражании
        axes.margins(x = 0,
                     y = 0.02,
                     tight = False)
        #Автоматическое масштабирование графика
        axes.autoscale(True,True,True)

        axes.set_facecolor(color='#f5f5f5')
        #fig.suptitle(f'График цены инструмента {figi}')
        axes.set_title(f'{self.y_info}',
                       loc='left',
                       fontstyle='oblique',
                       fontsize='medium',
                       color = '#595959')
        myFmt = mdates.DateFormatter('%m.%y')
        axes.xaxis.set_major_formatter(myFmt)
        axes.xaxis.label.set_color('#595959')
        axes.yaxis.label.set_color('#595959')
        axes.tick_params(colors='#595959', which='both')
        axes.spines['bottom'].set_color('#ebebeb')
        axes.spines['bottom'].set_linewidth(3)
        axes.spines['top'].set_color('#ebebeb')
        axes.spines['top'].set_linewidth(0)
        axes.spines['right'].set_color('#ebebeb')
        axes.spines['left'].set_color('#ebebeb')
        #Автоматическое масштабирование по осям
        axes.autoscale_view(tight=None, scalex=False, scaley=True)
        #Настройки отображения осей
        plt.xticks(rotation=35, ha='right')
        #Показать координаты последенй точки
        y_text=f'{y[-1][0]}\nТекущая цена'
        plt.annotate(y_text, xy=(x[-1], y[-1]+5),
                     textcoords='offset pixels',
                     xytext=(3,0),
                     ha='right')

        return fig

    def draw_candle_chart(self):
        '''Возвращает объект графика типа свечи
        '''
        figi = self.data[0]
        start_date = self.data[1]
        end_date = self.data[2]
        log.debug(f'{__name__} -> draw_candle_chart() -> start_date: {start_date}, end_date: {end_date}')
        data = DataProcessing(figi, start_date, end_date)
        raw_data_frame = data.get_local_stored_data()


        quotes = raw_data_frame[['open', 'high', 'low', 'close']]

        #Создадим объект графика
        fig, axes = plt.subplots(nrows=1,
                                 ncols=1,
                                 figsize=(10, 6),
                                 facecolor='#ebebeb', # Цвет в тон виджета
                                                      # на котором размещен график
                                 layout='constrained')
        #Определение отступов по осям в процентном выражании
        plt.margins(x=0,
                    y=0.02,
                    tight=False)
        #Автоматическое масштабирование графика
        plt.autoscale(True,True,True)
        #fig.tight_layout() #Отображать без подрезки осей

        #define width of candlestick elements
        candle_body_width = .4
        candle_tail_width = .05
        #define up and down prices
        up_data_frame = quotes[quotes.close>=quotes.open]
        down_data_frame = quotes[quotes.close<quotes.open]
        #define colors to use
        bar_up = 'green'
        bar_down = 'red'

        #plot up prices
        plt.bar(up_data_frame.index,
                up_data_frame.close-up_data_frame.open,
                candle_body_width, bottom=up_data_frame.open,
                color=bar_up,
                align='center')
        plt.bar(up_data_frame.index,
                up_data_frame.high-up_data_frame.close,
                candle_tail_width,
                bottom=up_data_frame.close,
                color=bar_up,
                align='center')
        plt.bar(up_data_frame.index,
                up_data_frame.low-up_data_frame.open,
                candle_tail_width,
                bottom=up_data_frame.open,
                color=bar_up,
                align='center')

        #plot down prices
        plt.bar(down_data_frame.index,
                down_data_frame.close-down_data_frame.open,
                candle_body_width,
                bottom=down_data_frame.open,
                color=bar_down,
                align='center')
        plt.bar(down_data_frame.index,
                down_data_frame.high-down_data_frame.open,
                candle_tail_width,
                bottom=down_data_frame.open,
                color=bar_down,
                align='center')
        plt.bar(down_data_frame.index,
                down_data_frame.low-down_data_frame.close,
                candle_tail_width,
                bottom=down_data_frame.close,
                color=bar_down,
                align='center')

        start_time = raw_data_frame.index[0].to_pydatetime().strftime('%d.%m.%y %H:%M')
        end_time = raw_data_frame.index[-1].to_pydatetime().strftime('%d.%m.%y %H:%M')
        #plt.title(f'Котировки {figi} \n {start_time} - {end_time}')
        plt.xlabel('Время')
        plt.ylabel('Цена')
        #rotate x-axis tick labels
        plt.xticks (rotation=45, ha='right')
        plt.grid(axis='x')
        plt.grid(axis='y')
        axes.set_facecolor(color='#f5f5f5')
        #fig.suptitle(f'График цены инструмента {figi}')
        axes.set_title(f'{self.y_info}',
                       loc='left',
                       fontstyle='oblique',
                       fontsize='medium',
                       color = '#595959')
        myFmt = mdates.DateFormatter('%m.%y')
        axes.xaxis.set_major_formatter(myFmt)
        axes.xaxis.label.set_color('#595959')
        axes.yaxis.label.set_color('#595959')
        axes.tick_params(colors='#595959', which='both')
        axes.spines['bottom'].set_color('#ebebeb')
        axes.spines['bottom'].set_linewidth(3)
        axes.spines['top'].set_color('#ebebeb')
        axes.spines['top'].set_linewidth(0)
        axes.spines['right'].set_color('#ebebeb')
        axes.spines['left'].set_color('#ebebeb')
        #Автоматическое масштабирование по осям
        axes.autoscale_view(tight=None, scalex=False, scaley=True)
        return fig

    def get_average_prices(self):
        '''Функция возвращает средние цены покупки продажи инструмента
        '''
        ticker = self.data[3]
        #Столбцы выборки
        cols_list = ["price"]
        where_filter = {"transaction_type": "Buy",
                        "ticker": ticker}
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("transactions").select(cols_list = cols_list, WHERE = where_filter)
        #log.debug(f'{__name__} -> get_average_price() -> sql_query: {sql_query}')
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        #log.debug(f'{__name__} -> get_average_price() -> средние цены:')
        #print(data)
        buy_value_list = []
        for i in range(len(data)):
                #log.debug(f'{__name__} -> get_average_price() -> type(item[0]): {type(data[i][0])}')
                buy_value_list.append(float(data[i][0]))
        #вычислим среднее значение покупок
        try:
            average_buy = sum(buy_value_list)/len(buy_value_list)
        except:
            average_buy = None

        cols_list = ["price"]
        where_filter = {"transaction_type": "Sell",
                        "ticker": ticker}
        #Создаем запрос к БД
        sql_query = ScriptNormalizer("transactions").select(cols_list = cols_list, WHERE = where_filter)
        #Создание подключения к БД
        db_connection = DBIntegration()
        #Отправка запроса
        data = DBIntegration.script_executer_with_return_data(db_connection,sql_query)
        sell_value_list = []
        for i in range(len(data)):
                sell_value_list.append(float(data[i][0]))

        try:
            average_sell = sum(sell_value_list)/len(sell_value_list)
        except:
            average_sell = None

        return average_buy, average_sell

