from datetime import datetime
from matplotlib import pyplot as plt
from numpy import flatiter
import pandas as pd
import pickle
import sys
import os
#Добавим папку уровнем выше в пространство имен
new_work_dir=os.path.abspath(os.path.join(__file__ ,"../.."))
sys.path.append(new_work_dir)

from chart_lib.chart import MyChart

import logging
logging.basicConfig(level=logging.DEBUG,
                    #filemode='a',
                    #filename='test_chart_log.log',
                    format="%(asctime)s-%(levelname)s> !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!%(message)s")


def redraw_line_chart():
    '''Обновление графика с новыми параметрами из полей окна
    '''
    figi = 'TCS00A106540'
    start_date = datetime(2022, 11, 15, 22, 1, 47, 124639)
    end_date = datetime(2023, 11, 15, 22, 1, 47, 124639)
    data = (figi, start_date, end_date, 'RU000A106540')
    chart = MyChart(data, 'test')
    fig = chart.draw_line_chart()
    print(os.getcwd())
    print(f'type(fig): {type(fig)}')
    return fig

def try_draw_waffle_chart():
    data = (1,1,1)
    chart = MyChart(data, 'test')
    chart.draw_waffle_chart()

#fig = redraw_line_chart()
#plt.plot(fig)
#plt.show()

if __name__ == '__main__':
    try_draw_waffle_chart()