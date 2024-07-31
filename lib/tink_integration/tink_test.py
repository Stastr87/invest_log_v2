from Auth import Auth
from google.protobuf.timestamp_pb2 import Timestamp
from operations_servise import Operations
from pprint import pprint

def get_token():
    token=Auth.get_trading_token_from_file(Auth)
    return token



body={"account_id":"2176241723",
      "start":'2023-03-01T00:00:00Z',
      "end":'2023-03-10T00:00:00Z',
      "state":1,
      "figi":"BBG004S68614"
}
request=Operations(TOKEN=get_token(),BODY=body)

data=request.get_my_operations()

pprint(data)