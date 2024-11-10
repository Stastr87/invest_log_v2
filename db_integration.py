import time, sys, os, psycopg2, platform, logging

import config
logger_config = config.get_logger_config()

if 'wind' in str(platform.system()).lower():
    db_integration_log_path = logger_config['path']
else:
    db_integration_log_path = logger_config['alternative_path']

db_integration_log_file = logger_config['db_integration']['name']
file_mode = logger_config['db_integration']['mode']
logger_level = logger_config['db_integration']['level']

# Настройка логирования
log_db_integration = logging.getLogger(__name__)
if logger_level.lower() == 'debug':
    log_db_integration.setLevel(logging.DEBUG)
if logger_level.lower() == 'error':
    log_db_integration.setLevel(logging.ERROR)
if logger_level.lower() == 'info':
    log_db_integration.setLevel(logging.INFO)
if logger_level.lower() == 'warning':
    log_db_integration.setLevel(logging.WARNING)
if logger_level.lower() == 'critical':
    log_db_integration.setLevel(logging.CRITICAL)
if logger_level == None:
    log_db_integration.setLevel(logging.NOTSET)
formatter = logging.Formatter(u"[%(asctime)s] [%(levelname)s] %(message)s")
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(formatter)
fh = logging.FileHandler(filename=os.path.join(db_integration_log_path,
                                               db_integration_log_file),
                         mode=file_mode,
                         encoding='utf-8')
fh.setFormatter(formatter)
log_db_integration.handlers.clear()
log_db_integration.addHandler(sh)
log_db_integration.addHandler(fh)



class DBIntegration:
    '''Класс описывающий взаимодействие с БД
    '''
    def __init__(self):
        current_config = config.get_config()

        if current_config["use_local_db"]:
            db_config = current_config["local_db"]
        else:
            db_config = current_config["remote_db"]

        self.db = db_config['database']
        self.user = db_config['db_user']
        self.password = db_config['db_password']
        self.host = db_config['db_host']
        self.port = db_config['db_port']
        self.set_connection()

    def set_connection(self): ## Функция создания соединения
        self.connection = psycopg2.connect(database=self.db,
                                           user=self.user,
                                           password=self.password,
                                           host=self.host,
                                           port=self.port)
        log_db_integration.debug(f'{__class__} {__name__} -> set_connection() -> Соединене с БД установлено')

    def script_executer_with_commit(self, script):
        '''Запускает SQL скрипт
        '''
        cur = self.connection.cursor()
        cur.execute(script)
        self.connection.commit()

    def script_executer_with_return_data(self, script):
        '''Запускает SQL скрипт. Возвращает данные в результате его выполнения

        Query the database and obtain data as Python objects
        https://www.psycopg.org/docs/usage.html
        '''
        cur = self.connection.cursor()
        cur.execute(script)
        data = cur.fetchall()
        return data

    def __del__(self):
        time.sleep(0.5)
        self.connection.close()
        log_db_integration.debug(f'{__class__} {__name__} -> Соединене с БД закрыто')
