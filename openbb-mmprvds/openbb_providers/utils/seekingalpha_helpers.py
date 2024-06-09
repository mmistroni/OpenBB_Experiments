import logging
from datetime import date, datetime
import feedparser
from pandas.tseries.offsets import BDay


def get_seekingalpha_stock_ideas():
    return _generate_initial_feeds('https://seekingalpha.com/feed/stock-ideas')

def get_seekingalpha_dividend_picks():
    return _generate_initial_feeds('https://seekingalpha.com/feed/dividends/editors-picks')

def _generate_initial_feeds(feed_url):
    d = feedparser.parse(feed_url)
    holder = []
    for item in d['entries']:
        ticker = item.get('category', '')
        title = item.get('title', '')
        link = item.get('link', '')
        pub_date = item['published_parsed']
        cob = date(pub_date.tm_year, pub_date.tm_mon, pub_date.tm_mday)
        holder.append(dict(as_of_date=cob, tickers=ticker, detail=title, link=link))
    return holder


