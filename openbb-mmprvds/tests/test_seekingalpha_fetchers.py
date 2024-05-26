"""Pyth2 Fetchers tests."""
import pytest
from openbb_providers.models.seekingalpha import SeekingAlphaData, SADividendPicksFetcher, SAStockIdeaFetcher
from openbb_core.app.service.user_service import UserService
import re
import requests
from bs4 import BeautifulSoup


test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)

def response_filter(response):
    if "Location" in response["headers"]:
        response["headers"]["Location"] = [
            re.sub(r"apikey=[^&]+", "apikey=MOCK_API_KEY", x)
            for x in response["headers"]["Location"]
        ]
    return response

@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("apikey", "MOCK_API_KEY"),
        ],
        "before_record_response": response_filter,
    }

#
@pytest.mark.record_http
def test_sa_stock_ideas(credentials=test_credentials):
    params = {}
    fetcher = SAStockIdeaFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

@pytest.mark.record_http
def test_sa_dividend_picks(credentials=test_credentials):
    params = {}
    fetcher = SADividendPicksFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

def test_sa_data():

    test_dict = {'as_of_date': '2024-05-17',
                  'tickers': 'FTAI',
                  'detail': 'ftai aviation: still a buy after stock price doubles',
                  'link': 'https://seekingalpha.com/article/4694208-ftai-aviation'
                 }


    sa = SeekingAlphaData(**test_dict)

    assert sa.tickers == test_dict['tickers']
    assert sa.as_of_date == test_dict['as_of_date']
    assert sa.detail == test_dict['detail']
    assert sa.link == test_dict['link']

