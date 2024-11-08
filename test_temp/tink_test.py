import os
from pprint import pprint
import sys
#Добавим папку уровнем выше в пространство имен
new_work_dir=os.path.abspath(os.path.join(__file__ ,"../.."))
sys.path.append(new_work_dir)
#Импорт модулей из директории выше уровнем

from auth.token import Token
from services.operations_service.operations_service import Operations
from services.instruments_service.instruments_service import InstrumentsService

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)
fh = logging.FileHandler(filename=os.path.join('log', 'tink_test.log'), mode='a')
fh.setFormatter(formatter)
logger.handlers.clear()
logger.addHandler(sh)
logger.addHandler(fh)


class MyTestClass:
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)



        logger.info(f'{self.__class__.__name__} Started')
        self.set_token()
        self.instrements_service_test()
        self.operations_service_test()
        logger.info(f'{self.__class__.__name__} Finished')

    def set_token(self):
        token = Token()
        self.token = token.access_token

    def instrements_service_test(self):
        request = InstrumentsService(TOKEN=self.token)
        data = request.get_etf_list()
        logger.info(f'instrements_service_test() -> GET some data from T service... type(data): {type(data)}')

    def operations_service_test(self):
        request = Operations(TOKEN=self.token)
        data = request.test_func()
        logger.info(f'operations_service_test() -> GET some data from T service... type(data): {type(data)}')

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    MyTestClass()