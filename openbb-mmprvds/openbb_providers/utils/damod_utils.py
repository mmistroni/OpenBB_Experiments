from bs4 import BeautifulSoup
import requests
from datetime import date, datetime
import random

def get_industry_multiples(year=None):
    baseUrl = 'https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/psdata.html'
    histUrl = 'https://pages.stern.nyu.edu/~adamodar/New_Home_Page/dataarchived.html#multiples'


