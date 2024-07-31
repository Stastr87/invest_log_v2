from __future__ import print_function

import tink_requests
from InstrumentsDB import InstrumentsDB

etf_list=tink_requests.market_etfs_get_data()
shares_list=tink_requests.market_shares_get_data()
bonds_list=tink_requests.market_bonds_get_data()
InstrumentsDB.insert_data(InstrumentsDB, shares_list)
InstrumentsDB.insert_data(InstrumentsDB, bonds_list)
InstrumentsDB.insert_data(InstrumentsDB, etf_list)