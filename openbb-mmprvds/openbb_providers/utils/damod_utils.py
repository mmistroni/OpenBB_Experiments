from bs4 import BeautifulSoup
import requests
from datetime import date, datetime
import random
from io import BytesIO
import pandas as pd
import logging

'''
Prof A Damodaran's industry datasets.
https://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/variable.htm

Company By Industry here :https://www.stern.nyu.edu/~adamodar/pc/datasets/indname.xls

All these functions will return 'measures' at industry level

'''

psRatiosUrlTTM = 'https://www.stern.nyu.edu/~adamodar/pc/datasets/psdata.xls'
betasBySectorTTM = 'https://www.stern.nyu.edu/~adamodar/pc/datasets/betas.xls'
fundgrowepsTTM = 'https://www.stern.nyu.edu/~adamodar/pc/datasets/fundgr.xls'
roeTTM = 'https://www.stern.nyu.edu/~adamodar/pc/datasets/roe.xls'
peRatiosTTM = 'https://www.stern.nyu.edu/~adamodar/pc/datasets/pedata.xls'
pvDataTTM = 'https://www.stern.nyu.edu/~adamodar/pc/datasets/pbvdata.xls'
instHoldingTTM  = 'https://www.stern.nyu.edu/~adamodar/pc/datasets/inshold.xls'

def _get_data(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        xls_file = BytesIO(response.content)
        return pd.read_excel(xlsFile, sheet_name=1, header=7)
    except Exception as e:
        logging.info(f'Failed to fetch {url}:{str(e)}')
        raise Exception(f'Failed to fetch {url}:{str(e)}')

def get_valuation_metrics(num_years->int = None):
    '''
       use async to retrieve all valuation metrics 
    '''
    pass


def get_roe():
    '''
    Return on Equity by Sector (US)
    https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/roe.html
    '''
    return _get_data(roeTTM)
    
    
def get_ps():
    '''
    Revenue Multiples by Sector (US)
    https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/psdata.html
    '''
    return _get_data(psRatiosUrlTTM)

def get_fgrowtheps():
    '''
    Fundamental Growth in EPS by Sector (US)
    https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/fundgr.html
    '''
    return _get_data(fundgrowepsTTM)

def get_pe():
    '''
    PE Ratio by Sector (US)
    https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/pedata.html
    '''
    return _get_data((peRatiosTTM))

def get_betas():
    '''
    Betas by Sector (US)
    https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html
    '''
    return _get_data(betasBySectorTTM)

def get_pvdata():
    '''
    Price and Value to Book Ratio by Sector (US)
    https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/pbvdata.html
    '''
    return _get_data(pvDataTTM)

def get_institutional_holders():
    '''
    Institutional Holding By Industry
    https://people.stern.nyu.edu/adamodar/New_Home_Page/datafile/inshold.html
    '''
    return _get_data(instHoldingTTM)

