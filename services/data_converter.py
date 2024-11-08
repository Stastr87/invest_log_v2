# import config
# from  my_logger import MyLogger
# logger_config = config.get_logger_config()
# log_file = logger_config['data_converter']
# log = MyLogger(log_file).new_logger


class DataConverter(object):
    def __init__(self):
        pass

    def tink_quotation_to_float(self,raw_data):
        '''Конвертирует данные типа Quotation
        в тип float
        '''
        quotation = raw_data
        units = float(quotation.units)
        if quotation.nano > 0:
            nano = quotation.nano*10**-9
        else:
            nano = 0
        value = units + nano
        return value

    def tink_money_value_to_float(self,raw_data):
        '''Конвертирует данные типа MoneyValue
        в тип float
        '''
        #logging.debug(f'{__name__} -> tink_money_value_to_float() -> raw_data: {raw_data}')
        money_value = raw_data
        units = float(money_value.units)
        if money_value.nano != 0:
            nano = money_value.nano*10**-9
        else:
            nano = 0
        value = units+nano
        #logging.debug(f'{__name__} -> tink_money_value_to_float() -> value: {value}')
        return value