from __future__ import print_function
import json
from pprint import pprint
from typing import List


class Auth:
    def get_trading_token_from_file(self) -> List[list]:
        file=open('.\\top_secret\\top_secret.json')
        data=file.read()
        json_data=json.loads(data)
        tokens=json_data['tokens']
        token=None
        for item in tokens:
            if item['type']=='trading':
                token=item['token']
        return token
