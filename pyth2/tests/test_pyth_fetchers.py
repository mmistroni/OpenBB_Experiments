"""Pyth2 Fetchers tests."""
import pytest
from openbb_pyth2.models.fetchers import ExampleFetcher, ExampleData
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
@pytest.mark.skip(reason='temp')
def test_ExampleFetcher(credentials=test_credentials):
    params = {"symbol": "AAPL", "limit": 5, "use_cache": False}
    fetcher = ExampleFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
@pytest.mark.skip(reason='temp')
def test_ExampleFetcherNoLimit(credentials=test_credentials):
    params = {"symbol": "AAPL",  "use_cache": False}
    fetcher = ExampleFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
@pytest.mark.skip(reason='temp')
def test_ExampleData():

    test_dict = {'symbol': 'AAPL', 'date': '2024-02-27', 'marketCap': 2844761945830}

    ed = ExampleData(**test_dict)

    print(f'{ed.marketCap}')

@pytest.mark.record_http
def test_fetch_http_data_vcr(credentials=test_credentials):
    params = {"symbol": "AAPL", "limit": 5, "use_cache": False}
    fetcher = ExampleFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


