import os
from tinkoff.invest import Client, schemas
from google.protobuf.timestamp_pb2 import Timestamp
from pprint import pprint
from datetime import datetime
import time

import my_logger
log = my_logger.setup_applevel_logger(file_name = 'operations_service.log')

class Operations:
    '''OperationsService
    Сервис предназначен для получения:
    1. списка операций по счёту;
    2. портфеля по счёту;
    3. позиций ценных бумаг на счёте;
    4. доступного остатка для вывода средств;
    5. получения различных отчётов.
    '''
    def __init__(self, **kwargs):

        self.token=None
        if "TOKEN" in kwargs.keys():
            self.token=kwargs["TOKEN"]

        self.request_body=None
        if "BODY" in kwargs.keys():
            self.request_body=kwargs["BODY"]


    def get_my_operations_by_account(self):
        ''' Возвращает спикок операций по переданному списку счетов
        '''
        account_id_list=self.request_body["account_id_list"]
        response_data_list=[]
        for account_id_item in account_id_list:
            account_id=account_id_item
            start=self.request_body["start"]
            start=datetime.strptime(start, '%Y-%m-%dT%H:%M:%S%z')
            from_=start
            end=self.request_body["end"]
            end=datetime.strptime(end, '%Y-%m-%dT%H:%M:%S%z')
            to=end
            state=schemas.OperationState(self.request_body["state"])
            with Client(self.token) as client:
                data=client.operations.get_operations(account_id=account_id,
                                                      from_=from_,
                                                      to=to,
                                                      state=state)
            response_data_list.append(data)
            time.sleep(1)

        return response_data_list

    def get_my_positions_by_account(self):
        ''' Возвращает список активов на переданных списком счетах
        элемент списка словарь вида:
            {"account_id":account_id,
            "positions":<Массив объектов tinkoff.invest.PositionsResponse>}
        '''
        account_id_list=self.request_body["account_id_list"]
        response_data_list=[]
        for account_id_item in account_id_list:
            account_id=account_id_item
            with Client(self.token) as client:
                data=client.operations.get_positions(account_id=account_id)
                positions_by_account={"account_id":account_id,
                                       "positions":data}
                response_data_list.append(positions_by_account)
        return response_data_list


    def get_my_positions(self):
        ''' Возвращает список активов на переданных списком счетах
        '''
        account_id_list=self.request_body["account_id_list"]
        response_data_list=[]
        for account_id_item in account_id_list:
            account_id=account_id_item
            with Client(self.token) as client:
                data=client.operations.get_positions(account_id=account_id)
                response_data_list.append(data)
        return response_data_list