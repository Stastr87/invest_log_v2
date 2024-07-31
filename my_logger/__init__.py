import logging
import sys
import os
#Добавим папку уровнем выше в пространство имен
new_work_dir=os.path.abspath(os.path.join(__file__ ,"../.."))
sys.path.append(new_work_dir)

import config
logger_config = config.get_logger_config()

APP_LOGGER_NAME = logger_config['app_logger_name']
logger_level = logger_config['level']

def setup_applevel_logger(logger_name = APP_LOGGER_NAME, file_name = None):
    logger = logging.getLogger(logger_name)

    if logger_level.lower() == 'debug':
        logger.setLevel(logging.DEBUG)
    if logger_level.lower() == 'error':
        logger.setLevel(logging.ERROR)
    if logger_level.lower() == 'info':
        logger.setLevel(logging.INFO)
    if logger_level.lower() == 'warning':
        logger.setLevel(logging.WARNING)
    if logger_level.lower() == 'critical':
        logger.setLevel(logging.CRITICAL)
    if logger_level == None:
        logger.setLevel(logging.NOTSET)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(sh)

    if file_name:
        if not os.path.isdir('logs'):
            os.mkdir('logs')
        fh = logging.FileHandler(os.path.abspath(os.path.join('logs', file_name)))
        print(f"my_logger add data to file: {os.path.abspath(os.path.join('logs', file_name))}")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger

def get_logger(module_name):
   return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)