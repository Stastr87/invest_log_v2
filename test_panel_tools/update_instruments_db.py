import os
import sys
#Добавим папку уровнем выше в пространство имен
new_work_dir=os.path.abspath(os.path.join(__file__ ,"../.."))
sys.path.append(new_work_dir)


from db_integration import DBIntegration
from sql_lib.script_normalizer import ScriptNormalizer
from auth.token import Token
from pprint import pprint

import my_logger
log = my_logger.setup_applevel_logger(file_name = 'update_instruments_db.log')

def get_token():
    token = Token()
    return token.access_token

def get_instruments():
    #Столбцы выборки
    cols_list=["figi"]
    #Параметр сортировки
    #order=["ticker_name","ASC"]
    #Шаблон значений в ячейках для выборки поиск по всем таблицам
    #search_template={"ticker":f"{self.ui.ticker_edit.text()}"}
    #Ограничение вариантов выборки
    #limit=10
    #Создаем запрос к БД
    sql_query=ScriptNormalizer("instruments").select(cols_list=cols_list)
    log.info(f'{__name__}. {sql_query}')
    #Создание подключения к БД
    db_connection=DBIntegration()
    #Отправка запроса
    data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
    log.info(f'{__name__}.data: {data}')
    return data


db_data=get_instruments()
figi_list=[]
for item in db_data:
    figi_list.append(item[0])
pprint(figi_list)

'''
for item in response_data:
    pprint(item)
    if item["account_id"] not in accounts_id_list:

        sql_query=ScriptNormalizer("accounts", new_data=item).insert()
        #Создание подключения к БД
        db_connection=DBIntegration()
        DBIntegration.script_executer_with_commit(db_connection,sql_query)
'''


