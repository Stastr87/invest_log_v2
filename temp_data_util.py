'''Модуль содержит вспомогательные функции для работы с временными данными
'''
import shelve

#Logging
import my_logger
log = my_logger.setup_applevel_logger(file_name = 'temp_data_util.log')

def get_stored_data(temp_file):
    '''Возвращает дату последнего обновления и
       список позиций на эту дату из временного файла
    '''
    shelveFile = shelve.open(temp_file)
    positions_storage = shelveFile['positions_info']
    last_update = positions_storage['last_update']
    log.debug(f'{__name__} -> get_stored_data() -> last_update: {last_update}')
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