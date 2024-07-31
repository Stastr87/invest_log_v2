from __future__ import print_function


from Auth import Auth

from openapi_client import openapi
from pprint import pprint


def get_token():
    token=Auth.get_trading_token_from_file(Auth)
    return token

def market_shares_get_data():
    #Запрос данных с сервера
    client = openapi.api_client(get_token())
    shares_list_data = client.market.market_stocks_get()
    shares_list=shares_list_data.payload.instruments

    return shares_list

def market_bonds_get_data():
    client = openapi.api_client(get_token())
    bonds_list_data=client.market.market_bonds_get()
    bonds_list=bonds_list_data.payload.instruments
    return bonds_list

def market_etfs_get_data():
    client = openapi.api_client(get_token())
    etf_list_data = client.market.market_etfs_get()
    etf_list=etf_list_data.payload.instruments
    return etf_list



