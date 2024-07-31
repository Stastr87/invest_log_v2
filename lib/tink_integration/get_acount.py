import os
from tinkoff.invest import Client
from Auth import Auth
from pprint import pprint

def get_token():
    token=Auth.get_trading_token_from_file(Auth)
    return token


def get_account_data():
    with Client(get_token()) as client:
        data=client.users.get_accounts()
    return data
