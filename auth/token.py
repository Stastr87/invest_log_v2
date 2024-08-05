from __future__ import print_function
import json
import os
#import logging

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
            #logging.debug(f'{__name__}: Ошибка получения токена из переменных окружения', exc_info=True)
            print(f'{__name__}: Ошибка получения токена из переменных окружения')

        try:
            #Устаревший способ хранить в файле
            file = 'key.json'
            new_work_dir = os.path.abspath(os.path.join(__file__ ,"../.."))
            file_path = os.path.join(new_work_dir,'auth',file)
            with open (file_path, 'r') as file:
                data = file.read()
                json_data = json.loads(data)
                token = json_data['api_key']
            return token
        except:
            #logging.debug(f'{__name__}: Ошибка получения токена из файла', exc_info=True)
            print(f'{__name__}: Ошибка получения токена из из файла')

