"""Pyth2 Fetchers tests."""
import pytest
from openbb_providers.models.fmp_marketcap import FMPMarketCapData, FMPMarketCapDataFetcher
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
@pytest.mark.vcr()
def test_fmp_marketcap_fetcher_no_limit(credentials=test_credentials):
    params = {"symbol": "AAPL", "use_cache": False}
    fetcher = FMPMarketCapDataFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

@pytest.mark.vcr()
def test_fmp_marketcap_fetcher_with_limit(credentials=test_credentials):
    params = {"symbol": "AAPL", "limit" : 50, "use_cache": False}
    fetcher = FMPMarketCapDataFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

def test_fmp_data():

    test_dict = {'date': '2024-01-30 00:00:00', 'symbol': 'AAPL',
                 'marketCap': 12345}

    mc = FMPMarketCapData(**test_dict)

    assert mc.symbol == test_dict['symbol']
    assert mc.date == test_dict['date']
    assert mc.marketcap == test_dict['marketCap']

