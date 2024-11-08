from __future__ import print_function
import datetime
from datetime import datetime
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
    some_connection.close()
    print ('\nСоедиенение закрыто')


class DBLib:
    def insert_data(table,data) -> List[list]:

        keys=list(data.keys())
        keys=str(keys).replace('[','').replace(']','').replace("'",'"')
        values=list(data.values())
        values=str(values).replace('[','').replace(']','')

        new_connection=open_connection(database, user, password, host, port)
        cur = new_connection.cursor()
        cur.execute(f"INSERT INTO public.{table}({keys}) VALUES ({values});")
        new_connection.commit()
        print("Операция завершена")
        close_connection(new_connection)

    '''В объектно-ориентированном программировании деструктор 
    вызывается при удалении или уничтожении объекта.
    Деструктор используется для выполнения действий по очистке 
    перед разрушением объекта, таких как закрытие соединений с базой данных.
    Для выполнения задачи очистки перед удалением объекта в Python используется
    метод __del__().При удалении ссылки на объект деструктор не запускается.
    Для этого нужно удалить все ссылки на этот объект.'''
    def __del__(self):
        print('Object destroyed')