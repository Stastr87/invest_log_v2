import os
from tinkoff.invest import Client, schemas
from google.protobuf.timestamp_pb2 import Timestamp
from pprint import pprint
from datetime import datetime

class Accounts:
    '''
    Сервис предназначен для получения:
    1. списка счетов пользователя;
    2. маржинальных показателей по счёту.
    '''
    def __init__(self, **kwargs):

        self.token=None
        if "TOKEN" in kwargs.keys():
            self.token=kwargs["TOKEN"]

        self.request_body=None
        if "BODY" in kwargs.keys():
            self.request_body=kwargs["BODY"]


    def get_my_accounts(self):
        with Client(self.token) as client:
            data=client.users.get_accounts()
        data_list=[]
        for account in data.accounts:
            data={"account_id":str(account.id),
                  "account_name":account.name,
                  "brocker_name":"Тиньков"}
            data_list.append(data)
        return data_list

    '''
    from __future__ import print_function
from pprint import pprint
import get_acount
from DBLib import DBLib

account_data=get_acount.get_account_data()


for account in account_data.accounts:
    pprint(f'id: {account.id} name: {account.name}')
    data={"account_id":str(account.id),
          "account_name":account.name}
    DBLib.insert_data("accounts",data)

    '''