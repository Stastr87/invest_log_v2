from enum import Enum
import os
from pyclbr import Class
from tinkoff.invest import Client, schemas
from google.protobuf.timestamp_pb2 import Timestamp
from pprint import pprint
from datetime import datetime
import time

import my_logger
log = my_logger.setup_applevel_logger(file_name = 'operations_service.log')

class OperationTypes(Enum):
    OPERATION_TYPE_UNSPECIFIED = 0 # (0, 'Тип операции не определён')
    OPERATION_TYPE_INPUT = 1 # (1, 'Пополнение брокерского счёта')
    OPERATION_TYPE_BOND_TAX = 2 # (2, 'Удержание НДФЛ по купонам')
    OPERATION_TYPE_OUTPUT_SECURITIES = 3 # (3, 'Вывод ЦБ')
    OPERATION_TYPE_OVERNIGHT = 4 # (4, 'Доход по сделке РЕПО овернайт')
    OPERATION_TYPE_TAX = 5 # (5, 'Удержание налога')
    OPERATION_TYPE_BOND_REPAYMENT_FULL = 6 # (6, 'Полное погашение облигаций')
    OPERATION_TYPE_SELL_CARD = 7 # (7,' Продажа ЦБ с карты')
    OPERATION_TYPE_DIVIDEND_TAX = 8 # (8, 'Удержание налога по дивидендам')
    OPERATION_TYPE_OUTPUT = 9 # (9, 'Вывод денежных средств')
    OPERATION_TYPE_BOND_REPAYMENT = 10 # (10, 'Частичное погашение облигаций')
    OPERATION_TYPE_TAX_CORRECTION = 11 # (11, 'Корректировка налога')
    OPERATION_TYPE_SERVICE_FEE = 12 # (12, 'Удержание комиссии за обслуживание брокерского счёта')
    OPERATION_TYPE_BENEFIT_TAX = 13 # (13, 'Удержание налога за материальную выгоду')
    OPERATION_TYPE_MARGIN_FEE = 14 # (14, 'Удержание комиссии за непокрытую позицию')
    OPERATION_TYPE_BUY = 15 # (15, 'Покупка ЦБ')
    OPERATION_TYPE_BUY_CARD = 16 # (16, 'Покупка ЦБ с карты')
    OPERATION_TYPE_INPUT_SECURITIES = 17 # (17, 'Перевод ценных бумаг из другого депозитария')
    OPERATION_TYPE_SELL_MARGIN = 18 # (18, 'Продажа в результате Margin-call')
    OPERATION_TYPE_BROKER_FEE = 19 # (19, 'Удержание комиссии за операцию')
    OPERATION_TYPE_BUY_MARGIN = 20 # (20,' Покупка в результате Margin-call')
    OPERATION_TYPE_DIVIDEND = 21 # (21, 'Выплата дивидендов')
    OPERATION_TYPE_SELL = 22 # (22, 'Продажа ЦБ')
    OPERATION_TYPE_COUPON = 23 # (23, 'Выплата купонов')
    OPERATION_TYPE_SUCCESS_FEE = 24 # (24, 'Удержание комиссии SuccessFee')
    OPERATION_TYPE_DIVIDEND_TRANSFER = 25 # (25, 'Передача дивидендного дохода')
    OPERATION_TYPE_ACCRUING_VARMARGIN = 26 # (26, 'Зачисление вариационной маржи')
    OPERATION_TYPE_WRITING_OFF_VARMARGIN = 27 # (27, 'Списание вариационной маржи')
    OPERATION_TYPE_DELIVERY_BUY = 28 # (28, 'Покупка в рамках экспирации фьючерсного контракта')
    OPERATION_TYPE_DELIVERY_SELL = 29 # (29, 'Продажа в рамках экспирации фьючерсного контракта')
    OPERATION_TYPE_TRACK_MFEE = 30 # (30, 'Комиссия за управление по счёту автоследования')
    OPERATION_TYPE_TRACK_PFEE = 31 # (31, 'Комиссия за результат по счёту автоследования')
    OPERATION_TYPE_TAX_PROGRESSIVE = 32 # (32, 'Удержание налога по ставке 15%')
    OPERATION_TYPE_BOND_TAX_PROGRESSIVE = 33 # (33, 'Удержание налога по купонам по ставке 15%')
    OPERATION_TYPE_DIVIDEND_TAX_PROGRESSIVE = 34 # (34, 'Удержание налога по дивидендам по ставке 15%')
    OPERATION_TYPE_BENEFIT_TAX_PROGRESSIVE = 35 # (35, 'Удержание налога за материальную выгоду по ставке 15%')
    OPERATION_TYPE_TAX_CORRECTION_PROGRESSIVE = 36 # (36, 'Корректировка налога по ставке 15%')
    OPERATION_TYPE_TAX_REPO_PROGRESSIVE = 37 # (37, 'Удержание налога за возмещение по сделкам РЕПО по ставке 15%')
    OPERATION_TYPE_TAX_REPO = 38 # (38, 'Удержание налога за возмещение по сделкам РЕПО')
    OPERATION_TYPE_TAX_REPO_HOLD = 39 # (39, 'Удержание налога по сделкам РЕПО')
    OPERATION_TYPE_TAX_REPO_REFUND = 40 # (40, 'Возврат налога по сделкам РЕПО')
    OPERATION_TYPE_TAX_REPO_HOLD_PROGRESSIVE = 41 # (41, 'Удержание налога по сделкам РЕПО по ставке 15%')
    OPERATION_TYPE_TAX_REPO_REFUND_PROGRESSIVE = 42 # (42, 'Возврат налога по сделкам РЕПО по ставке 15%')
    OPERATION_TYPE_DIV_EXT = 43 # (43, 'Выплата дивидендов на карту')
    OPERATION_TYPE_TAX_CORRECTION_COUPON = 44 # (44, 'Корректировка налога по купонам')
    OPERATION_TYPE_CASH_FEE = 45 # (45, 'Комиссия за валютный остаток')
    OPERATION_TYPE_OUT_FEE = 46 # (46, 'Комиссия за вывод валюты с брокерского счета')
    OPERATION_TYPE_OUT_STAMP_DUTY = 47 # (47, 'Гербовый сбор')
    OPERATION_TYPE_OUTPUT_SWIFT = 50 # (50, 'SWIFT-перевод')
    OPERATION_TYPE_INPUT_SWIFT = 51 # (51, 'SWIFT-перевод')
    OPERATION_TYPE_OUTPUT_ACQUIRING = 53 # (53, 'Перевод на карту')
    OPERATION_TYPE_INPUT_ACQUIRING = 54 # (54, 'Перевод с карты')
    OPERATION_TYPE_OUTPUT_PENALTY = 55 # (55, 'Комиссия за вывод средств')
    OPERATION_TYPE_ADVICE_FEE = 56 # (56, 'Списание оплаты за сервис Советов')
    OPERATION_TYPE_TRANS_IIS_BS =  57 # (57, 'Перевод ценных бумаг с ИИС на Брокерский счет')
    OPERATION_TYPE_TRANS_BS_BS = 58 # (58, 'Перевод ценных бумаг с одного брокерского счета на другой')
    OPERATION_TYPE_OUT_MULTI = 59 # (59, 'Вывод денежных средств со счета')
    OPERATION_TYPE_INP_MULTI = 60 # (60, 'Пополнение денежных средств со счета')
    OPERATION_TYPE_OVER_PLACEMENT = 61 # (61, 'Размещение биржевого овернайта')
    OPERATION_TYPE_OVER_COM = 62 # (62, 'Списание комиссии')
    OPERATION_TYPE_OVER_INCOME = 63 # (63, 'Доход от оверанайта')
    OPERATION_TYPE_OPTION_EXPIRATION = 64 # (64, 'Экспирация')

    def __init__(self, num):
        self.num = num

    def get_translation(self):
       """Возвращает тектовый формат операции на русском языке"""
       if self.num==0:
           return 'Тип операции не определён'
       if self.num==1:
           return 'Пополнение брокерского счёта'
       if self.num==2:
           return 'Удержание НДФЛ по купонам'
       if self.num==3:
           return 'Вывод ЦБ'
       if self.num==4:
           return 'Доход по сделке РЕПО овернайт'
       if self.num==5:
           return 'Удержание налога'
       if self.num==6:
           return 'Полное погашение облигаций'
       if self.num==7:
           return 'Продажа ЦБ с карты'
       if self.num==8:
           return 'Удержание налога по дивидендам'
       if self.num==9:
           return 'Вывод денежных средств'
       if self.num==10:
           return 'Частичное погашение облигаций'
       if self.num==11:
           return 'Корректировка налога'
       if self.num==12:
           return 'Удержание комиссии за обслуживание брокерского счёта'
       if self.num==13:
           return 'Удержание налога за материальную выгоду'
       if self.num==14:
           return 'Удержание комиссии за непокрытую позицию'
       if self.num==15:
           return 'Покупка ЦБ'
       if self.num==16:
           return 'Покупка ЦБ с карты'
       if self.num==17:
           return 'Перевод ценных бумаг из другого депозитария'
       if self.num==18:
           return 'Продажа в результате Margin-call'
       if self.num==19:
           return 'Удержание комиссии за операцию'
       if self.num==20:
           return 'Покупка в результате Margin-call'
       if self.num==21:
           return 'Выплата дивидендов'
       if self.num==22:
           return 'Продажа ЦБ'
       if self.num==23:
           return 'Выплата купонов'
       if self.num==24:
           return 'Удержание комиссии SuccessFee'
       if self.num==25:
           return 'Передача дивидендного дохода'
       if self.num==26:
           return 'Зачисление вариационной маржи'
       if self.num==27:
           return 'Списание вариационной маржи'
       if self.num==28:
           return 'Покупка в рамках экспирации фьючерсного контракта'
       if self.num==29:
           return 'Продажа в рамках экспирации фьючерсного контракта'
       if self.num==30:
           return 'Комиссия за управление по счёту автоследования'
       if self.num==31:
           return 'Комиссия за результат по счёту автоследования'
       if self.num==32:
           return 'Удержание налога по ставке 15%'
       if self.num==33:
           return 'Удержание налога по купонам по ставке 15%'
       if self.num==34:
           return 'Удержание налога по дивидендам по ставке 15%'
       if self.num==35:
           return 'Удержание налога за материальную выгоду по ставке 15%'
       if self.num==36:
           return 'Корректировка налога по ставке 15%'
       if self.num==37:
           return 'Удержание налога за возмещение по сделкам РЕПО по ставке 15%'
       if self.num==38:
           return 'Удержание налога за возмещение по сделкам РЕПО'
       if self.num==39:
           return 'Удержание налога по сделкам РЕПО'
       if self.num==40:
           return 'Возврат налога по сделкам РЕПО'
       if self.num==41:
           return 'Удержание налога по сделкам РЕПО по ставке 15%'
       if self.num==42:
           return 'Возврат налога по сделкам РЕПО по ставке 15%'
       if self.num==43:
           return 'Выплата дивидендов на карту'
       if self.num==44:
           return 'Корректировка налога по купонам'
       if self.num==45:
           return 'Комиссия за валютный остаток'
       if self.num==46:
           return 'Комиссия за вывод валюты с брокерского счета'
       if self.num==47:
           return 'Гербовый сбор'
       if self.num==50:
           return 'SWIFT-перевод'
       if self.num==51:
           return 'SWIFT-перевод'
       if self.num==53:
           return 'Перевод на карту'
       if self.num==54:
           return 'Перевод с карты'
       if self.num==55:
           return 'Комиссия за вывод средств'
       if self.num==56:
           return 'Списание оплаты за сервис Советов'
       if self.num==57:
           return 'Перевод ценных бумаг с ИИС на Брокерский счет'
       if self.num==58:
           return 'Перевод ценных бумаг с одного брокерского счета на другой'
       if self.num==59:
           return 'Вывод денежных средств со счета'
       if self.num==60:
           return 'Пополнение денежных средств со счета'
       if self.num==61:
           return 'Размещение биржевого овернайта'
       if self.num==62:
           return 'Списание комиссии'
       if self.num==63:
           return 'Доход от оверанайта'
       if self.num==64:
           return 'Экспирация'
       else:
           return f'{self.num} тип операции не определен'



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
        ''' Возвращает список операций по переданному списку счетов
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
            time.sleep(0.3)

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