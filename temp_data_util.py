#Модуль содержит вспомогательные функции для работы с временными данными

import shelve, os, sys
from enum import Enum
from services.data_converter import DataConverter

import config
logger_config = config.get_logger_config()
logger_path = logger_config['path']
temp_data_util_log_file = logger_config['temp_data_util']['name']
file_mode = logger_config['temp_data_util']['mode']
logger_level = logger_config['temp_data_util']['level']

import logging
# Настройка логирования
log_temp_data_util = logging.getLogger(__name__)
if logger_level.lower() == 'debug':
    log_temp_data_util.setLevel(logging.DEBUG)
if logger_level.lower() == 'error':
    log_temp_data_util.setLevel(logging.ERROR)
if logger_level.lower() == 'info':
    log_temp_data_util.setLevel(logging.INFO)
if logger_level.lower() == 'warning':
    log_temp_data_util.setLevel(logging.WARNING)
if logger_level.lower() == 'critical':
    log_temp_data_util.setLevel(logging.CRITICAL)
if logger_level == None:
    log_temp_data_util.setLevel(logging.NOTSET)
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)
fh = logging.FileHandler(filename=os.path.join(logger_path, temp_data_util_log_file), mode=file_mode, encoding='utf-8')
fh.setFormatter(formatter)
log_temp_data_util.handlers.clear()
log_temp_data_util.addHandler(sh)
log_temp_data_util.addHandler(fh)

converter = DataConverter()

class CurrencyTypes(Enum):
    xau = 'BBG000VJ5YR4'
    usd = 'BBG0013HGFT4'
    cny = 'BBG0013HRTL0'

def get_stored_data(temp_file):
    '''Возвращает дату последнего обновления и
       список позиций на эту дату из временного файла
    '''
    shelveFile = shelve.open(temp_file)
    positions_storage = shelveFile['positions_info']
    last_update = positions_storage['last_update']
    # log.debug(f'{__name__} -> get_stored_data() -> last_update: {last_update}')
    return last_update, positions_storage

def get_normalized_positions_list(positions_info):
    '''Возвращает список позиций в нормальзиванном
    формате для отображения в таблице главного окна
    '''
    normalized_positions_list = list()
    for item in positions_info:
        securities_list = item["positions"].securities
        for security in securities_list:
            normalized_position = {"figi":security.figi,
                                   "quantity":int(security.balance),
                                   "account_id":item["account_id"]}
            normalized_positions_list.append(normalized_position)

    return normalized_positions_list


def get_currencies_positions_list(positions_info):
    '''Возвращает список валют и друг металлов на счетах
    '''
    money_positions_list = list()

    for item in positions_info:
        money_list = item["positions"].money
        log_temp_data_util.debug(f'[{__name__}] get_currencies_positions_list() -> money_list {money_list}')
        if money_list:
            # for money_item in money_list:
            #     for currency_item in CurrencyTypes:
            #         if currency_item == money_item.currency:
            for money_item in money_list:
                for iso_currency in CurrencyTypes:
                    if money_item.currency == iso_currency.name:
                        normalized_position = {"figi":iso_currency.value,
                                               "quantity":converter.tink_money_value_to_float(money_item),
                                               "account_id":item["account_id"]}
                        money_positions_list.append(normalized_position)

    log_temp_data_util.debug(f'[{__name__}] get_currencies_positions_list() -> currencies_list {money_positions_list}')

    return money_positions_list