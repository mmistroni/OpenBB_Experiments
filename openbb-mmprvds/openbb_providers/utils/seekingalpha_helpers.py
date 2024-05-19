import logging
from datetime import date, datetime
from bs4 import BeautifulSoup
import requests
from pandas.tseries.offsets import BDay


def get_seekingalpha_stock_ideas():
    return _generate_initial_feeds('https://seekingalpha.com/feed/stock-ideas')

def get_seekingalpha_dividend_picks():
    return _generate_initial_feeds('https://seekingalpha.com/feed/dividends/editors-picks')

def _extract_data(item):
    cats = item.find_all('category')
    ticks = ','.join(c.get_text() for c in cats)
    title = item.title.get_text().lower()
    link = item.guid.get_text()
    itemDate = item.pubdate.get_text()
    try:
        dt = datetime.strptime(itemDate, '%a, %d %b %Y %H:%M:%S %z').date()
    except Exception as e:
        logging.info('Failed to parse date{}'.format(itemDate))
        dt = date.today()
    return (ticks, title, link, dt)

def _generate_initial_feeds(feed_url):
    logging.info('Parsing URL:{}'.format(feed_url))
    page = requests.get(feed_url)
    soup = BeautifulSoup(page.content, 'lxml')
    items = soup.find_all('item')
    mapped = map(lambda i: _extract_data(i), items)
    holder = []
    for item in mapped:
        ticks = item[0]
        detail = item[1]
        link = item[2]
        pubDate = item[3]
        test_date = (date.today() - BDay(5)).date()
        if pubDate < test_date :
            logging.info('Skipping obsolete :{}({}) -  for {}'.format(pubDate, test_date, item))
            continue;
        date_str = pubDate.strftime('%Y-%m-%d')
        holder.append(dict(as_of_date=date_str, tickers=ticks, detail=detail, link=link))
    logging.info('returning:{}'.format(holder))
    return holder


