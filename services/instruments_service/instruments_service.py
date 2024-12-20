
from tinkoff.invest import Client
from tinkoff.invest.exceptions import RequestError
from datetime import datetime
from auth.token import Token


# import config
# logger_config = config.get_logger_config()
# logger_path = logger_config['path']
# log_file = logger_config['instruments_service']
# logger_level = logger_config['level']

# import logging
# logger = logging.getLogger(__name__)
# formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
# sh = logging.StreamHandler(sys.stdout)
# sh.setFormatter(formatter)
# fh = logging.FileHandler(filename=(log_file+log_file), mode=logger_config['mode'])
# fh.setFormatter(formatter)
# logger.handlers.clear()
# logger.addHandler(sh)
# logger.addHandler(fh)


def set_token():
    token = Token()
    return token.access_token


class InstrumentsService:
    """Сервис предназначен для получения информации об инструментах
    """

    def __init__(self, **kwargs):
        # logger.info(f'{self.__class__.__name__} initialized!!!')

        self.token= set_token()
        self.request_body=None
        if "BODY" in kwargs.keys():
            self.request_body=kwargs["BODY"]

    def get_bond_by_figi(self,figi):
        """Метод возвращает данные об инструменте типа Bond
        по его figi идентификатору
        """
        with Client(self.token) as client:
            try:
                # log_instruments_service.info(f'{__name__} -> try to get_bond_by_figi() -> figi: {figi}')
                response_data=client.instruments.bond_by(id_type=1, id=figi)
            except RequestError:
                response_data=None
                # log_instruments_service.error(f'{__name__} -> get_bond_by_figi() -> {e}')

        return response_data

    def get_bond_coupons_list(self,figi):
        """GetBondCoupons метод возвращает массив объектов типа Coupon
        """
        with Client(self.token) as client:
            try:
                # log_instruments_service.info(f'{__name__} -> try to get_bond_coupons() -> figi: {figi}')
                response_data=client.instruments.get_bond_coupons(figi=figi)
            except RequestError:
                response_data=None
                # log_instruments_service.error(f'{__name__} -> get_bond_coupons() -> {e}')
        return response_data

    def get_nearest_coupon(self,figi):
        """ Метод возвращает дату ближайшего купона и его величину в формате MoneyValue:
        nearest_coupon_date, nearest_coupon_money_value
        """

        nearest_coupon_date, nearest_coupon_money_value = None, None
        coupons_list_response = self.get_bond_coupons_list(figi)
        coupons_list = coupons_list_response.events
        now = datetime.now().timestamp()
        future_coupon_list=[]
        for i in range(len(coupons_list)):
            if coupons_list[i].coupon_date.timestamp() > now:
                future_coupon_list.append(coupons_list[i])

        for i in range(len(future_coupon_list)):
            if future_coupon_list[i].coupon_number<future_coupon_list[i-1].coupon_number:
                nearest_coupon_date = future_coupon_list[len(future_coupon_list)-1].coupon_date
                nearest_coupon_money_value = future_coupon_list[len(future_coupon_list)-1].pay_one_bond

        return nearest_coupon_date, nearest_coupon_money_value

    def get_currencies(self):
        """Метод возвращает список валют на рынке,
        имеющих статус 1 (Базовый список инструментов (по умолчанию).
        Инструменты доступные для торговли через TINKOFF INVEST API.)
        """

        with Client(self.token) as client:
            response_data = client.instruments.currencies(instrument_status=1)
        return response_data

    def get_currency_by(self,income_id: str):
        """Метод получения валюты по её идентификатору
        """
        with Client(self.token) as client:
            response_data=client.instruments.currency_by(id_type=1,id=income_id)
        return response_data

    def get_instrument_by(self,income_id: str):
        """GetInstrumentBy
        Метод получения основной информации об инструменте.
        Тело запроса — InstrumentRequest https://tinkoff.github.io/investAPI/instruments/#instrumentrequest
        Тело ответа — InstrumentResponse https://tinkoff.github.io/investAPI/instruments/#instrumentresponse
        """
        with Client(self.token) as client:
            response_data=client.instruments.get_instrument_by(id_type=1,id=income_id)
        return response_data

    def get_shares_list(self):
        """Получить список всех акций доступных к торговле
        """
        with Client(self.token) as client:
            shares_response = client.instruments.shares()
        instruments_list = shares_response.instruments
        return instruments_list

    def get_bonds_list(self):
        """Получить список всех облигаций доступных к торговле
        """
        with Client(self.token) as client:
            bonds_response = client.instruments.bonds()
        instruments_list=bonds_response.instruments
        return instruments_list

    def get_etf_list(self):
        """Получить список всех фондов доступных к торговле
        """
        with Client(self.token) as client:
            etfs_response = client.instruments.etfs()
        instruments_list = etfs_response.instruments
        return instruments_list

    def get_currencies_list(self):
        """Получить список всех валют доступных к торговле
        """
        with Client(self.token) as client:
            currency_response = client.instruments.currencies()
        instruments_list = currency_response.instruments
        return instruments_list