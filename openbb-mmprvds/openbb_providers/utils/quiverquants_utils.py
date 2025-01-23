from bs4 import BeautifulSoup
import requests
from datetime import date, datetime
import random
import logging
from io import BytesIO
import pandas as pd

'''
QuiverQuants Utils to scrape data from quiver quants

'''

_GOVCONTRACTS = 'https://www.quiverquant.com/sources/govcontracts'
_UATSTRINGS =  [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0", \
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko", \
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36" \
        ]

def _get_data(url):
    try:
        ua = random.choice(_UATSTRINGS)
        r = requests.get(url, headers={'User-Agent' : ua})
        return BeautifulSoup(r.content, 'html.parser')
    except Exception as e:
        logging.info(f'Failed to fetch {url}:{str(e)}')
        raise Exception(f'Failed to fetch {url}:{str(e)}')

def get_government_contracts():
    '''
    Return Government Contracts
    https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/roe.html
    '''
    bs = _get_data(_GOVCONTRACTS)
    tbl = bs.find('table', {'id' : 'myTable'})
    trs = tbl.find_all('tr')
    holders = []
    idx = 0
    for row in trs[1:]:
        try:
            tds = row.find_all('td')
            ticker = tds[0].find('a').text
            cob = tds[1].text
            amount = tds[2].text
            funding_ag = tds[3].text
            desc = tds[4].text
            holders.append(dict(ticker=ticker, asofdate=cob, amount=amount, funding_agency=funding_ag, description=desc))
        except Exception as e:
            logging.info('Unabble to extract data from:{row}')
  
    return pd.DataFrame(data=holders)


    
