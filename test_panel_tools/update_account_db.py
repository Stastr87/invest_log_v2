import os
import sys
#Добавим папку уровнем выше в пространство имен
new_work_dir=os.path.abspath(os.path.join(__file__ ,"../.."))
sys.path.append(new_work_dir)

from services.accounts_service.accounts_service import Accounts
from db_integration import DBIntegration
from sql_lib.script_normalizer import ScriptNormalizer
from auth.token import Token
from pprint import pprint

# import my_logger
# log = my_logger.setup_applevel_logger(file_name = 'update_account_db.log')

def get_token():
    token = Token()
    return token.access_token

def get_accounts():
    sql_query=ScriptNormalizer("accounts").select()
    # log.debug(f'{__name__}. {sql_query}')
    #Создание подключения к БД
    db_connection=DBIntegration()
    #Отправка запроса
    data=DBIntegration.script_executer_with_return_data(db_connection,sql_query)
    # log.debug(f'{__name__}.data: {data}')
    return data


request=Accounts(TOKEN=get_token())
response_data=request.get_my_accounts()
pprint(response_data)

db_data=get_accounts()
accounts_id_list=[]
for item in db_data:
    accounts_id_list.append(str(item[0]))

for item in response_data:
    pprint(item)
    if item["account_id"] not in accounts_id_list:

        sql_query=ScriptNormalizer("accounts", new_data=item).insert()
        #Создание подключения к БД
        db_connection=DBIntegration()
        DBIntegration.script_executer_with_commit(db_connection,sql_query)



