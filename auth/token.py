from __future__ import print_function
import json
import os
from pprint import pprint

import my_logger
log = my_logger.setup_applevel_logger(file_name = 'auth.log')


class Token(object):
    def __init__(self):
        self.access_token=self.get_trading_token()


    def get_trading_token(self):
        #Устаревший способ хранить в файле
        token = None
        try:
            if not token:
                # возьмем токен из переменных окружения
                token = os.environ.get('TINK_TOKEN')
                return token
        except:
            log.debug(f'{__name__}: Ошибка получения токена из переменных окружения', exc_info=True)

        try:
            #Устаревший способ хранить в файле
            file = 'key.json'
            new_work_dir = os.path.abspath(os.path.join(__file__ ,"../.."))
            file_path = os.path.join(new_work_dir,'top_secret',file)
            with open (file_path, 'r') as file:
                data = file.read()
            json_data = json.loads(data)
            token = json_data['api_key']
            return token
        except:
            log.debug(f'{__name__}: Ошибка получения токена из файла', exc_info=True)

