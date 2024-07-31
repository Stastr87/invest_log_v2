from __future__ import print_function
from pprint import pprint
import get_acount
from DBLib import DBLib

account_data=get_acount.get_account_data()


for account in account_data.accounts:
    pprint(f'id: {account.id} name: {account.name}')
    data={"account_id":str(account.id),
          "account_name":account.name}
    DBLib.insert_data("accounts",data)