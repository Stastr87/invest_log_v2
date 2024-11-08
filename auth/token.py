from __future__ import print_function
import json
import os, platform, sys, os

import config
logger_config = config.get_logger_config()

if 'wind' in str(platform.system()).lower():
    log_path = logger_config['path']
else:
    log_path = logger_config['alternative_path']

log_file_name = 'auth.log'
file_mode = 'a'
logger_level = 'debug'

import logging
# Настройка логирования
log_auth = logging.getLogger(__name__)
if logger_level.lower() == 'debug':
    log_auth.setLevel(logging.DEBUG)
if logger_level.lower() == 'error':
    log_auth.setLevel(logging.ERROR)
if logger_level.lower() == 'info':
    log_auth.setLevel(logging.INFO)
if logger_level.lower() == 'warning':
    log_auth.setLevel(logging.WARNING)
if logger_level.lower() == 'critical':
    log_auth.setLevel(logging.CRITICAL)
if logger_level == None:
    log_auth.setLevel(logging.NOTSET)
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)
fh = logging.FileHandler(filename=os.path.join(log_path,
                                               log_file_name),
                                               mode=file_mode,
                                               encoding='utf-8')
fh.setFormatter(formatter)
log_auth.handlers.clear()
log_auth.addHandler(sh)
log_auth.addHandler(fh)

class Token(object):
    def __init__(self):
        self.access_token = self.get_trading_token()

    def get_trading_token(self):
        #Устаревший способ хранить в файле
        token = None
        log_auth.debug(f'try to get token from system environment...')
        try:
            if not token:
                # возьмем токен из переменных окружения
                token = os.environ.get('TINK_TOKEN')
                log_auth.debug(f'get token from system environment success')
                if not token:
                    raise ValueError('Возвращено пустое значение')
                else:
                    return token

        except:
            log_auth.debug(f'{__name__}: Ошибка получения токена из переменных окружения', exc_info=True)
            # print(f'{__name__}: Ошибка получения токена из переменных окружения')

        log_auth.debug(f'try to get token from file...')
        try:
            #Устаревший способ хранить в файле
            file_path = '/Users/st/codeSpace_Python/invest_log/v2/auth/key.json'
            # new_work_dir = os.path.abspath(os.path.join(__file__ ,"../.."))
            # file_path = os.path.join(new_work_dir,'auth',file)
            with open (file_path, 'r') as file:
                data = file.read()
                json_data = json.loads(data)
                token = json_data['api_key']
            log_auth.debug(f'get token from file success')
            log_auth.debug(f'token {token[:5]}...')
            return token

        except:
            log_auth.debug(f'{__name__}: Ошибка получения токена из файла', exc_info=True)
            # print(f'{__name__}: Ошибка получения токена из из файла')

