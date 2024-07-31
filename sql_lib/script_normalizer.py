import json
from pprint import pprint

import my_logger
log = my_logger.setup_applevel_logger(file_name='D:\Python_code_space\InvestLog_v2\logs\script_normalizer.log')


class ScriptNormalizer:
    '''Класс нормализатор данных для формирования скриптов
    для взаимодействия с БД инструментов
    '''
    def __init__(self, table, **kwargs):
        log.debug(f'[{__name__}] -> called')
        if "date" in kwargs.keys():
            sql_date=kwargs["date"].replace(".","-")
            kwargs["date"]=sql_date

        self.table=table

        if kwargs is None:
            log.debug(f'[{__name__}] -> Параметры kwargs не переданы')
        else:
            for kwarg_name, data in kwargs.items():
                if kwarg_name == "new_data":
                    self.data=data
                    #log.debug(f'[{__name__}] -> self.data: {self.data}')

    def insert(self):
        #log.debug(f'[{__name__}] -> insert() ')

        keys_list=list(self.data.keys())
        #log.debug(f'[{__name__}] -> keys_list: {keys_list}')

        if len(keys_list)==1:
            keys = keys_list[0]
        else:
            keys=str(keys_list).replace('[','').replace(']','').replace("'",'"')

        values_list=list(self.data.values())
        #На случай если в значении поля типа "строка" попадется апостров или ковычки их необходимо удалить
        for i in range(len(values_list)):
            #pprint(f"values[{i}] {values[i]} type {type(values[i])}")
            if type(values_list[i])==str:
               values_list[i]=values_list[i].replace("'","").replace('"',"")
        values_str = str(values_list).replace('[','').replace(']','')
        #for value in values_list:
        #    clear_value = str(value).replace("'","").replace('"',"")
        #    values += f"{clear_value} "
        #log.debug(f'[{__name__}] -> values: {values}')
        script=f"INSERT INTO public.{self.table}({keys}) VALUES ({values_str});"
        #log.debug(f'[{__name__}] -> insert() script: {script}')
        return script

    def like_construstor(template_object):
        #Обрабатывается шаблон текста в столбцах выборки
        keys_list=list(template_object.keys())
        log.debug(f'[{__name__}] -> keys_list: {keys_list}')
        if len(keys_list)==1:
            query_template=f"LOWER({keys_list[0]}) LIKE LOWER('{template_object[keys_list[0]]}') OR"
        else:
            query_template_list = list()
            for i in range(len(keys_list)):
                query_template_list.append(f"LOWER({keys_list[i]}) LIKE LOWER('{template_object[keys_list[i]]}')")
                log.debug(f'[{__name__}] -> query_template_list: {query_template_list}')

            query_template=''
            for i in range(len(query_template_list)):
               query_template=query_template+f' {query_template_list[i]} OR'

        like_query=f" WHERE {query_template[:-3]}"
        log.debug(f'[{__name__}] -> like_construstor: {like_query}')
        return like_query

    def where_constructor(template_object):
        keys_list=list(template_object.keys())
        log.debug(f'[{__name__}] -> [where_constructor()] -> keys_list: {keys_list}')

        additional_query_template=''

        if len(keys_list)==1:
            where_query=f" WHERE {keys_list[0]}={template_object[keys_list[0]]}"
            # Если переданное значение - строка то его нужно поместить в ковычки
            if type(template_object[keys_list[0]]) == str:
                where_query=f" WHERE {keys_list[0]}='{template_object[keys_list[0]]}'"

        else:
            where_query=f" WHERE"

            query_template_list=[]
            for i in range(len(keys_list)):
                # Если переданное значение - строка то его нужно поместить в ковычки
                if type(template_object[keys_list[i]]) == str:
                    query_template_list.append(f"{keys_list[i]}='{template_object[keys_list[i]]}'")
                else:
                    query_template_list.append(f"{keys_list[i]}={template_object[keys_list[i]]}")
            log.debug(f"[{__name__}] -> [where_constructor()] -> query_template_list: {query_template_list}")

            # Если переданное значение - строка то его нужно поместить в ковычки
            if type(template_object[keys_list[0]]) == str:
                additional_query_template=f" {keys_list[0]}='{template_object[keys_list[0]]}'"
            else:
                additional_query_template=f" {keys_list[0]}={template_object[keys_list[0]]}"

            for i in range(1,len(query_template_list)):
               additional_query_template=additional_query_template+f" AND {query_template_list[i]}"

            where_query=where_query+additional_query_template
            log.debug(f"[{__name__}] -> [where_constructor()] -> where_query: {where_query}")

        return where_query

    def condition_constructor(template_object):
        keys_list=list(template_object.keys())
        log.debug(f'[{__name__}] -> [condition_constructor()] -> keys_list: {keys_list}')

        additional_query_template=''

        if len(keys_list)==1:
            condition_query=f" {keys_list[0]} {template_object[keys_list[0]]}"

        else:
            condition_query=f" "

            query_template_list=[]
            for i in range(len(keys_list)):
                query_template_list.append(f"{keys_list[i]} {template_object[keys_list[i]]}")

            log.debug(f'[{__name__}] -> [condition_constructor()] -> query_template_list: {query_template_list}')

            additional_query_template=f" {keys_list[0]} {template_object[keys_list[0]]}"
            for i in range(1,len(query_template_list)):
               additional_query_template=additional_query_template+f' AND {query_template_list[i]}'

            condition_query=condition_query+additional_query_template
            log.debug(f'[{__name__}] -> [condition_constructor()] -> condition_query: {condition_query}')

        return condition_query

    def date_query_constructor(period):
        end_date=period["end_date"]
        start_date=period["start_date"]
        query_template=f" WHERE date_time<'{end_date}' AND date_time>'{start_date}'"
        return query_template

    def join_constructor(self, obj):
        log.debug(f'[{__name__}] -> join_constructor is running')

        ''' example
        SELECT accounts.account_name, instruments.ticker_name
        FROM transactions
        JOIN accounts ON transactions.brocker_account=CAST (accounts.account_id as character varying)
        JOIN instruments ON transactions.ticker_guid=instruments.id;
        '''
        target_list=obj["target"]
        source_tables=obj["source"]
        keys_list=list(source_tables.keys())
        log.debug(f'[{__name__}] -> keys_list: {keys_list}')
        query_template_list=[]
        for i in range(len(keys_list)):
            for item in source_tables[keys_list[i]]:
                if item=='account_id':
                    query_template_list.append(f" JOIN {keys_list[i]} ON {self.table}.{target_list[i]}=CAST({keys_list[i]}.{item} as character varying)")
                else:
                    query_template_list.append(f" JOIN {keys_list[i]} ON {self.table}.{target_list[i]}={keys_list[i]}.{item}")


        query_template=''
        for i in range(len(query_template_list)):
            query_template=query_template+f'{query_template_list[i]}'

        log.debug(f'[{__name__}] -> query_template: {query_template}')
        return query_template

    def update(self, **kwargs):
        '''Функция формирует UPDATE запрос к БД

        UPDATE public.transactions
        SET memo='test', price='33'
        WHERE transaction_id=12;
        example:
            data={"instrument_memo": self.ui.description.toPlainText()}
            filter={"figi": f"'{self.ui.figi_label.text()}'"}
            sql_query=ScriptNormalizer("instruments", new_data=data,).update(WHERE=filter)
        '''
        log.debug(f'[{__name__}] -> [update()] ')

        keys=list(self.data.keys())
        script=f"UPDATE public.{self.table} SET"
        #Если передано больше одного ключа
        if len(keys)>1:
            for key in keys:
                script=script+f" {key}='{self.data[key]}',"
            script=script[:-1]
        else:
            script=script+f" {keys[0]}='{self.data[keys[0]]}'"


        where_query = str()
        if kwargs is None:
            log.debug(f'[{__name__}] -> [update()] -> Параметры kwargs не переданы')
        else:
            for item, value in kwargs.items():
                if item == "WHERE":
                    where_query=ScriptNormalizer.where_constructor(value)
        log.debug(f'[{__name__}] -> [update()] -> where_query: \n{where_query}')
        script=f"{script}{where_query};"
        log.debug(f'[{__name__}] -> [update()] -> script: \n{script}')
        return script

    def select(self, **kwargs):
        '''Функция формирует SELECT запрос к БД
        '''

        like_query,order_query,limit_query,period_query,where_query,join_query,condition_query='','','','','','',''

        prefix_script=f"SELECT * FROM public.{self.table}"

        if kwargs is None:
            log.debug(f'[{__name__}] -> Параметры kwargs не переданы')
        else:
            for item, value in kwargs.items():
                if item == "cols_list":
                    #Обрабатывается список столбцов для выборки
                    cols=str(value).replace('[','').replace(']','').replace("'","")
                    prefix_script=f"SELECT {cols} FROM public.{self.table}"

            for item, value in kwargs.items():
                if item == "JOIN":
                    join_query=ScriptNormalizer.join_constructor(self, value)
                if item == "WHERE":
                    where_query=ScriptNormalizer.where_constructor(value)
                if item == "PERIOD":
                    period_query=ScriptNormalizer.date_query_constructor(value)
                if item == "LIKE":
                    like_query=ScriptNormalizer.like_construstor(value)
                if item == "ORDER":
                    #Обрабатывается список для сортировки вида [<имя столбца>,<порядок сортировки>]
                    order_query=f" ORDER BY {value[0]} {value[1]}"
                if item == "LIMIT":
                    #Обрабатывается значение для ограничения выборки
                    limit_query=f" LIMIT {value}"
                if item == "CONDITION":
                    condition_query=ScriptNormalizer.condition_constructor(value)

        if condition_query != '':
            script=f"{prefix_script}{join_query}{like_query}{period_query}{where_query} AND{condition_query}{order_query}{limit_query};"
        if where_query=='':
            script=f"{prefix_script}{join_query}{like_query}{period_query} WHERE{condition_query}{order_query}{limit_query};"
        if where_query=='' and condition_query=='':
            script=f"{prefix_script}{join_query}{like_query}{period_query}{order_query}{limit_query};"
        else:
            script=f"{prefix_script}{join_query}{like_query}{period_query}{where_query}{condition_query}{order_query}{limit_query};"
        log.debug(f'[{__name__}] -> [select()] -> script: {script}')
        return script