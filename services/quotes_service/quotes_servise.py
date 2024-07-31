import os
from pathlib import Path
import shelve
from tinkoff.invest import Client
from tinkoff.invest import schemas
from auth.token import Token
from pprint import pprint

import my_logger
log = my_logger.setup_applevel_logger(file_name = 'quotes_servise.log')

class MarketDataService:
    '''MarketDataService
    Данный сервис предназначен для получения различной (в т.ч. исторической)
    биржевой информации. Существует два варианта взаимодействия с сервисом
    котировок:
    * Unary-методы — данный вариант следует использовать в случаях,
    когда не требуется оперативность получения информации или для загрузки
    исторических данных. Существует ограничение на количество запросов в минуту,
    подробнее: Лимитная политика.
    * Bidirectional-stream — используется для получения биржевой информации в
    реальном времени с минимально возможными задержками. Для работы со
    стрим-соединениями также существуют ограничения, согласно лимитной политике.
    * Server-side-stream — используется для получения биржевой информации в реальном
    времени с минимально возможными задержками. В отличие от MarketDataStream в
    данном стриме передаётся объект, содержащий все типы подписок.
    ServerSideStream необходим для корректной трансляции маркетдаты в браузерные
    клиенты по gRPC-web, который не поддерживает bidirection стримы.
    Для работы со стрим-соединениями также существуют ограничения,
    согласно лимитной политике.
    Важно! В сервисе TINKOFF INVEST API для отображения цен облигаций и фьючерсов
    используются пункты. Для облигаций один пункт равен одному проценту номинала
    облигации. Для расчёта реальной стоимости фьючерса можно воспользоваться формулой:

    price / min_price_increment * min_price_increment_amount

    Формулы расчета реальной стоимости инструментов в валюте
    price — текущая котировка ценной бумаги;
    nominal — номинал облигации;
    min_price_increment — шаг цены;
    min_price_increment_amount — стоимость шага цены;
    lot - лотность инструмента.

    Акции
    price * lot

    Облигации
    Пункты цены для котировок облигаций представляют собой проценты номинала облигации. Для пересчёта пунктов в валюту можно воспользоваться формулой:
    price / 100 * nominal
    price / 100 * nominal + current_nkd Используется для подсчета с учетом НКД
    НКД - накопленный купонный доход. Может возвращаться в параметрах current_nkd или aci_value.

    Валюта
    price * lot / nominalc
    Важно! При торговле валютой необходимо учитывать, что такие валюты как Иена, Армянский драм и Тенге имеют nominal = 100

    Фьючерсы
    Стоимость фьючерсов так же предоставляется в пунктах, для пересчёта можно воспользоваться формулой:

    price / min_price_increment * min_price_increment_amount

    '''

    def __init__(self, **kwargs):
        self.token = self.set_token()
        self.request_body = None
        if "BODY" in kwargs.keys():
            self.request_body = kwargs["BODY"]

    def set_token(self):
        token = Token()
        return token.access_token

    def get_close_prices_request(self,some_instrument):
        '''GetClosePricesRequest
        Запрос цен закрытия торговой сессии по инструментам.

        Возвращает Цены закрытия торговой сессии по инструментам.
        Field            Type                                            Description
        close_prices     Массив объектов InstrumentClosePriceResponse    Массив по инструментам.

        В качестве аргумента Массив объектов InstrumentClosePriceRequest
        https://tinkoff.github.io/investAPI/marketdata/#instrumentclosepricerequest
        '''
        instrument_close_price_request_object=schemas.InstrumentClosePriceRequest('figi')
        instrument_close_price_request_object.instrument_id=some_instrument
        pprint(f'{instrument_close_price_request_object}: instrument_close_price_request_object')
        with Client(self.token) as client:
            response=client.market_data.get_close_prices(instruments=[instrument_close_price_request_object])
        return response

    def get_quotes_by_figi(self):
        ''' GetLastPrices
        Возвращает которивки инструментов по переданному листу figi
        '''
        figi_list=self.request_body["figi_list"]

        response_data_list=[]
        with Client(self.token) as client:
            try:
                response_data_list=client.market_data.get_last_prices(figi=figi_list)
                error_message="I'm fine"
            except:
                response_data_list=[]
                error_message="Something going wrong"

        return response_data_list, error_message

    def update_local_currencies(self):
        '''Обновляет котировки валюты в локальном файле
        для прикладных нужд по следующему списку:
        "BBG0013HGFT4" - USD/RUB
        '''

        figi_list=["BBG0013HGFT4"]
        with Client(self.token) as client:
            last_prices_list=client.market_data.get_last_prices(figi=figi_list)

        last_price_json_list=[]
        for item in last_prices_list.last_prices:
            item_price=str(f'{item.price.units},{item.price.nano}')
            last_price_json_item={"figi":item.figi,
                                  "price":item_price}
            last_price_json_list.append(last_price_json_item)
        #log.debug(f'{__name__} update_local_currencies -> last_price_json_list: {last_price_json_list}')

        #Сохраним данные во временном файле
        #Используется библиотека pathlib для
        #корректного присвоения путей в разных ОС
        temp_dir=Path("temp_data")
        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)
        temp_file=temp_dir/"temp"
        shelveFile=shelve.open(temp_file)
        shelveFile['currencies']=last_price_json_list
        shelveFile.close()

    def get_candle_array(self):
        '''
        Метод запроса исторических свечей по инструменту.
        Тело запроса — GetCandlesRequest https://tinkoff.github.io/investAPI/marketdata/#getcandlesrequest
        Тело ответа — GetCandlesResponse https://tinkoff.github.io/investAPI/marketdata/#getcandlesresponse
        Возвращает массив объектов HistoricCandle https://tinkoff.github.io/investAPI/marketdata/#historiccandle
        '''
        log.debug(f'{__name__} -> get_candle_array () -> self.request_body: {self.request_body}')
        with Client(self.token) as client:
            candle_array=client.market_data.get_candles(figi=self.request_body.figi,
                                                        from_=self.request_body.from_,
                                                        to=self.request_body.to,
                                                        interval=self.request_body.interval,
                                                        instrument_id=self.request_body.instrument_id)
        return candle_array

