from bs4 import BeautifulSoup
import requests
from datetime import date, datetime
from typing import Any, Dict, List, Optional
import asyncio
import random
from io import BytesIO
import pandas as pd
import logging
from collections import OrderedDict
'''

'''

_SECTOR_MAP = OrderedDict([('XLK', 'Technology'), ('XLF', 'Financials'), ('XLE', 'Energy'),
                                  ('XLV', 'Health Care'), ('XLI', 'Industrials'), ('XLP', 'Consumer Staples'),
                                  ('XLU', 'Utilities'), ('XLY', 'Consumer Discretionary'), ('XLB', 'Materials'),
                                  ('XLRE', 'Real Estate'), ('XLC', 'Communication Services'), ('^GSPC', 'S&P500')
                                  ])
    


_PERIOD_MAP = { '1d' : 1,
                '1w' : 5,
                '1m' : 20,
                '3m' : 60,
                '6m' : 120,
                '1y' : 220}


async def get_fmprep_historical(ticker: str, key:str, period:str, colname:str ='adjClose') -> List[Dict] :

    numdays = _PERIOD_MAP.get(period, 1)

    logging.info(f'period:{period}, days:{numdays}')
    hist_url = 'https://financialmodelingprep.com/api/v3/historical-price-full/{}?apikey={}'.format(ticker, key)
    data = requests.get(hist_url).json().get('historical')
    sector_name = _SECTOR_MAP[ticker]
    if data:
        # return a dataframe where all values are tickes
        return [dict(ticker=ticker, sector=sector_name, close=d[colname]) for d in data[:numdays]]
    raise Exception(f'No data found for {ticker}, {period}')

async def get_data_for_sector(sector: str, period:str, key:str) ->  List[Dict]:
    return get_fmprep_historical(sector, key, period)

async def get_sector_data(period:str, key:str) -> OrderedDict[str, List[Dict]] :
    sector_tickers = _SECTOR_MAP.keys()
    tasks = [get_data_for_sector(sector, period, key) for sector in sector_tickers]
    all_data = await asyncio.gather(*tasks)
    all_data_df = pd.concat(all_data, ignore_index=True)
    return all_data_df

    



