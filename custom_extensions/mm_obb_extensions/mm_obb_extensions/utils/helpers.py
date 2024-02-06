import requests
import os

def get_fmp_key() -> str :
    return ''    # we should get it from credentials


def get_fmp_marketcap(ticker : str, limit : int = 100) -> dict:
    key = get_fmp_key()
    base_url = f'https://financialmodelingprep.com/api/v3/historical-market-capitalization/{ticker}?limit={limit}&apikey={key}'
    data = requests.get(base_url).json()
    return data
