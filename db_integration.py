import time
import os
import json
import psycopg2
import config
import my_logger
log = my_logger.setup_applevel_logger(file_name = 'db_integration.log')

class DBIntegration:
    '''Класс описывающий взаимодействие с БД
    '''
    def __init__(self):
        self.db,self.user,self.password,self.host,self.port=self.get_config()

    def get_config(self):
        data=config.get_config()
        return data["database"], data["db_user"], data["db_password"], data["db_host"], data["db_port"]

    def open_connection(self): ## Функция создания соединения
        connection = psycopg2.connect(database=self.db,
                                      user=self.user,
                                      password=self.password,
                                      host=self.host,
                                      port=self.port)
        #log.debug(f'{__name__} -> open_connection -> Соединене с БД установлено')
        return connection

    def close_connection(some_connection): ## Функция закрытия соединения c таймером
        time.sleep(0.5)
        some_connection.close()
        #log.debug(f'{__name__} -> close_connection -> Соедиенение с БД закрыто')

    def script_executer_with_commit(self, script): ## Функция запуска скрипта
        new_connection=DBIntegration.open_connection(self)
        cur = new_connection.cursor()
        cur.execute(script)
        new_connection.commit()
        DBIntegration.close_connection(new_connection)


    def script_executer_with_return_data(self, script):
        '''Query the database and obtain data as Python objects
        https://www.psycopg.org/docs/usage.html
        '''
        new_connection=DBIntegration.open_connection(self)
        cur = new_connection.cursor()
        cur.execute(script)
        data=cur.fetchall()
        DBIntegration.close_connection(new_connection)
        return data