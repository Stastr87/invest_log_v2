
from __future__ import print_function
import datetime
from datetime import datetime
from openapi_client import openapi
from typing import List
from pprint import pprint
import time
import psycopg2

##--- вводные параметры соединения с БД---

database = "InvestLog"
user = "postgres"
password = "password"
host = "127.0.0.1"
port = "5432"

##---------------------------------------


def open_connection(db, usr, pas, hst, port): ## Функция создания соединения
    connection = psycopg2.connect(database=db,user=usr,password=pas,host=hst,port=port)
    print('\nСоединене с БД установлено')
    return connection

def close_connection(some_connection): ## Функция закрытия соединения c таймером
    time_count = 3
    print ('\nДо закрытия соедиенния осталось')
    for i in range(time_count,0,-1):
        print ('%d сек.'% i)
        time.sleep(1)
    some_connection.close()
    print ('\nСоедиенение закрыто')


class InstrumentsDB:
    def insert_data(self, incoming_shares_list) -> List[list]:
        shares_list=incoming_shares_list
        new_connection=open_connection(database, user, password, host, port)
        count=0
        for item in shares_list:
            #logging.debug(item)
            cur = new_connection.cursor()
            cur.execute("INSERT INTO public.instruments(ticker_name, ticker, instrument_type, figi, isin, min_price_increment, lot, currency) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" %(item.name.replace("'", "''"), item.ticker, item.type, item.figi, item.isin, item.min_price_increment, item.lot, item.currency))
            new_connection.commit()
            count+=1
            print(f'{count} Коммит записи {item.ticker}')

        print("Операция завершена")
        close_connection(new_connection)

