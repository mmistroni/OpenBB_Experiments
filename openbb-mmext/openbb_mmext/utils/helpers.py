import requests
import pandas as pd
import logging
import random
import math
from datetime import datetime
def get_nymo():
    return _get_mclellan('$NYMO')

def get_nysi():
    return _get_mclellan('$NYSI')

def _get_mclellan(ticker):
    try:
        YEARS = 25
        URL = f'https://stockcharts.com/c-sc/sc?s={ticker}&p=D&yr={YEARS}&mn=0&dy=0&i=t3757734781c&img=text&inspector=yes'
        data = requests.get(URL, headers={'user-agent': get_user_agent()}).text
        data = data.split('<pricedata>')[1].replace('</pricedata>', '')
        lines = data.split('|')
        data = []
        for line in lines:
            cols = line.split(' ')
            date = datetime(int(cols[1][0:4]), int(cols[1][4:6]), int(cols[1][6:8]))
            value = float(cols[3])

            if not math.isnan(value):
                data.append({'date': date, 'value': value})

        df = pd.DataFrame.from_dict(data)

        return {'AS_OF_DATE': date.today().strftime('%Y-%m-%d'),
                'LABEL': ticker,
                'VALUE': df.tail(1).to_dict('records')[0]['value']
                }
    except Exception as e:
        logging.info(f'Failed to get data for {ticker}:{str(e)}')
        {'AS_OF_DATE': date.today().strftime('%Y-%m-%d'),
         'LABEL': ticker,
         'VALUE': 0.0
         }

def get_user_agent():
    uastrings = [
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

    return random.choice(uastrings)


