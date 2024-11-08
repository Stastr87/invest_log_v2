
from __future__ import print_function
import datetime
from datetime import datetime
from typing import List
from pprint import pprint
import time
import psycopg2
import config

##--- вводные параметры соединения с БД---

# database = "InvestLog"
# user = "postgres"
# password = "password"
# host = "127.0.0.1"
# port = "5432"

##---------------------------------------

class InstrumentsDB:
    def insert_data(self, incoming_instruments_list) -> List[list]:
        self.config = config.get_config()
        new_connection = self.open_connection()
        count = 0
        for item in incoming_instruments_list:
            #logging.debug(item)
            cur = new_connection.cursor()
            cur.execute("INSERT INTO public.instruments(ticker_name, ticker, instrument_type, figi, isin, min_price_increment, lot, currency) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" %(item.name.replace("'", "''"), item.ticker, item.type, item.figi, item.isin, item.min_price_increment, item.lot, item.currency))
            new_connection.commit()
            count += 1
            print(f'{count} Коммит записи {item.ticker}')


    def open_connection(self): ## Функция создания соединения
        database, user, password, host, port = (self.config['database'],
                                                self.config['db_user'],
                                                self.config['db_password'],
                                                self.config['db_host'],
                                                self.config['db_port'])
        connection = psycopg2.connect(database=database,
                                      user=user,
                                      password=password,
                                      host=host,
                                      port=port)
        print('\nСоединене с БД установлено')
        return connection

    def __del__(self, connection_obj):
        time_count = 3
        print ('\nДо закрытия соедиенния осталось')
        for i in range(time_count,0,-1):
            print ('%d сек.'% i)
            time.sleep(1)
        connection_obj.close()
        print("Операция завершена")
        print ('\nСоедиенение закрыто')