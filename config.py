import json
import os


def get_config():
    if os.path.exists('config.json'):
        with open ('config.json') as file:
            data=file.read()
    else:
        new_work_dir=os.path.abspath(os.path.join(__file__ ,"../"))
        with open (os.path.join(new_work_dir,'config.json')) as file:
            data=file.read()
    json_data=json.loads(data)
    return json_data

def get_logger_config():
    if os.path.exists('logger_config.json'):
        with open ('logger_config.json') as file:
            data=file.read()
    else:
        new_work_dir=os.path.abspath(os.path.join(__file__ ,"../"))
        with open (os.path.join(new_work_dir,'logger_config.json')) as file:
            data=file.read()
    json_data=json.loads(data)
    return json_data