from site import abs_paths
import pandas as pd
import pickle
import os
from pprint import pprint
import sys
from datetime import datetime
from services.data_converter import DataConverter
#Добавим папку уровнем выше в пространство имен
new_work_dir=os.path.abspath(os.path.join(__file__ ,"../.."))
sys.path.append(new_work_dir)
#Импорт модулей из директории выше уровнем
from tinkoff.invest import Client, schemas
from services.quotes_service.quotes_servise import MarketDataService
from auth.token import Token

import my_logger
log = my_logger.setup_applevel_logger(file_name = 'data_processing_lib.log')


class DataProcessing(object):
    '''
        Для дальнейшего расширения функциональности необходимо реализовать ENUM:
        CANDLE_INTERVAL_UNSPECIFIED    0    Интервал не определён.
        CANDLE_INTERVAL_1_MIN    1    от 1 минуты до 1 дня.
        CANDLE_INTERVAL_5_MIN    2    от 5 минут до 1 дня.
        CANDLE_INTERVAL_15_MIN    3    от 15 минут до 1 дня.
        CANDLE_INTERVAL_HOUR    4    от 1 часа до 1 недели.
        CANDLE_INTERVAL_DAY    5    от 1 дня до 1 года.
        CANDLE_INTERVAL_2_MIN    6    от 2 минут до 1 дня.
        CANDLE_INTERVAL_3_MIN    7    от 3 минут до 1 дня.
        CANDLE_INTERVAL_10_MIN    8    от 10 минут до 1 дня.
        CANDLE_INTERVAL_30_MIN    9    от 30 минут до 2 дней.
        CANDLE_INTERVAL_2_HOUR    10    от 2 часов до 1 месяца.
        CANDLE_INTERVAL_4_HOUR    11    от 4 часов до 1 месяца.
        CANDLE_INTERVAL_WEEK    12    от 1 недели до 2 лет.
        CANDLE_INTERVAL_MONTH    13    от 1 месяца до 10 лет
        '''
    def __init__(self, figi, start_date=None, end_date=None):
        self._figi = figi
        self._start_date = start_date
        self._end_date = end_date
        self.timeFrame = schemas.CandleInterval(5)
        self.set_token()
        self.existing_array = self.get_existing_array(self.timeFrame)
        if self.existing_array.empty:
            self.tink_raw_candle_array = self.get_candle_array(self.timeFrame, self._start_date, self._end_date)
            raw_candle_array = self.tink_candles_to_data_frame(self.tink_raw_candle_array)
            self.save_data_to_local_storage(self.timeFrame, raw_candle_array)
        else:
            self.existing_start = self.existing_array.index[0].to_pydatetime()
            self.existing_end = self.existing_array.index[-1].to_pydatetime()
            #print(f'{__name__} -> self.existing_start: {self.existing_start} - self.existing_end: {self.existing_end}')
            #Если окажется что переданные даты выходят за рамки существующего массива данных то
            #Необходимо обновить архив данных
            if self.existing_start.timestamp()>self._start_date.timestamp() or self.existing_end.timestamp()<self._end_date.timestamp():
                self.update_data_in_local_storage()

    def set_token(self):
        token = Token()
        self._token = token.access_token

    def update_data_in_local_storage(self):
        ''' Обновляет локально сохраненные массивы данных
        '''
        # Разобъем запрос на 2 части:
        # Период "новая начальная дата" - "начальная сохраненная дата"
        # Период "Сохраненная конечная дата" - "Новая конечная дата"
        before_raw_candle_array = pd.DataFrame()
        after_raw_candle_array = pd.DataFrame()
        if self.existing_start.timestamp() > self._start_date.timestamp():
            log.debug(f'{__name__} -> update_data_in_local_storage() -> Обновление ранних данных')
            # В случае если запрос включает период больше года сервер данных возвращает ошибку
            # Необходио разбить интервал запроса на несколько отрезков и дописать
            # данные в локальное хранилище
            days_diff1 = self.existing_start.day - self._start_date.day
            if days_diff1 > 364:
                pass
            else:
                self.tink_raw_candle_array = self.get_candle_array(self.timeFrame, self._start_date, self.existing_start)
                before_raw_candle_array = self.tink_candles_to_data_frame(self.tink_raw_candle_array)

        if self.existing_end.timestamp() < self._end_date.timestamp():
            log.debug(f'{__name__} -> update_data_in_local_storage() -> Обновление поздних данных')
            days_diff2 = self._end_date.day - self.existing_end.day
            if days_diff2 > 364:
                pass

            else:
                self.tink_raw_candle_array = self.get_candle_array(self.timeFrame, self.existing_end, self._end_date)
                after_raw_candle_array = self.tink_candles_to_data_frame(self.tink_raw_candle_array)

        frames = [before_raw_candle_array,self.existing_array,after_raw_candle_array]
        result_frame = pd.concat(frames)
        log.debug(f'{__name__} -> update_data_in_local_storage() -> Сохранение данных в файл')
        self.save_data_to_local_storage(self.timeFrame, result_frame)


    def get_existing_array(self, timeFrame):
        '''Получаем таймфрейм и существующий массив данных по заданному таймфрейму
        '''
        candle_folder_name = os.path.join('candles',self._figi)
        new_work_dir = os.path.abspath(os.path.join(__file__ ,"../.."))
        raw_data_path = os.path.join(new_work_dir,candle_folder_name,f'{str(timeFrame)}_candles.pkl')

        try:
            with open (raw_data_path,'rb') as file:
                existing_array = pickle.load(file)
            log.debug(f'{__name__} -> get_existing_array() -> existing_array: Is exist')
        except:
            existing_array = pd.DataFrame()
            log.error(f'{__name__} -> get_existing_array() -> fail to open raw_data_path', exc_info=True)

        return existing_array


    def get_local_stored_data(self):
        """Возвращает массив данных согласно переданному через self
        отрезку времени
        """
        #Переделать под загрузку из файла согласно таймфрему
        raw_data_path = os.path.join('candles',self._figi,'5_candles.pkl')
        raw_data_path = os.path.abspath(raw_data_path)
        log.debug(f'{__name__} -> get_local_stored_data() -> raw_data_path: {raw_data_path}')
        with open(raw_data_path,'rb') as file:
            raw_data=pickle.load(file)

        #log.debug(f'{__name__} -> get_local_stored_data() -> type(raw_data.index): {type(raw_data.index)} type(self._end_date): {type(self._end_date)}')
        start_date = pd.to_datetime(self._start_date, utc = True)
        end_date = pd.to_datetime(self._end_date, utc = True)
        newdf = raw_data.loc[(raw_data.index > start_date) & (raw_data.index < end_date)]
        return newdf

    def get_candle_array(self, timeFrame,start,end):
        '''Тело запроса описывается в классом:
        class GetCandlesRequest(_grpc_helpers.Message):
            figi: str = _grpc_helpers.string_field(1)    # Deprecated Figi-идентификатор инструмента. Необходимо использовать instrument_id.
            from_: datetime = _grpc_helpers.message_field(2)    # Начало запрашиваемого периода в часовом поясе UTC.
            to: datetime = _grpc_helpers.message_field(3)    # Окончание запрашиваемого периода в часовом поясе UTC.
            interval: "CandleInterval" = _grpc_helpers.enum_field(4)    # Интервал запрошенных свечей. ENUM значение
            instrument_id: str = _grpc_helpers.string_field(5)    # Идентификатор инструмента, принимает значение figi или instrument_uid.
        '''
        body = schemas.GetCandlesRequest(figi=self._figi,
                                       from_=start,
                                       to=end,
                                       interval=timeFrame,
                                       instrument_id=self._figi)
        request = MarketDataService(TOKEN=self._token,BODY=body)
        candle_array = request.get_candle_array()
        return candle_array

    def save_data_to_local_storage(self, timeFrame, candle_array_data):
        # Сохранить данные во временном файле
        new_work_dir = os.path.abspath(os.path.join(__file__ ,"../.."))
        candle_folder_name = os.path.join('candles',self._figi)
        if not os.path.isdir(os.path.join(new_work_dir,candle_folder_name)):
            os.makedirs(os.path.join(new_work_dir,candle_folder_name))
        #Сохранить исходные данные (экземпляр класса) в pkl файле (модуль pikle)

        with open (os.path.join(new_work_dir,candle_folder_name,f'{str(timeFrame)}_candles.pkl'),'wb') as file:
            pickle.dump(candle_array_data,file)


    def tink_candles_to_data_frame(self, tink_raw_data):
        pd_frames = []
        raw_data = tink_raw_data.candles
        converter = DataConverter()
        for item in raw_data:
            open = converter.tink_quotation_to_float(item.open)
            high = converter.tink_quotation_to_float(item.high)
            low = converter.tink_quotation_to_float(item.low)
            close = converter.tink_quotation_to_float(item.close)
            volume = int(item.volume)
            time = item.time
            is_complete = item.is_complete
            df = pd.DataFrame({"open":open,"high": high,"low":low,"close":close,"volume":volume,"is_complete":is_complete},index=[time])
            pd_frames.append(df)
        try:
            total_df = pd.concat(pd_frames)
        except:
            total_df=pd.DataFrame()
            log.error(f'{__name__} -> tink_candles_to_data_frame() -> невозможно объединить данные', exc_info=True)

        return total_df