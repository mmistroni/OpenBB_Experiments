"""Pyth2 Fetchers tests."""
import pytest
from openbb_pyth2.models.fetchers import ExampleFetcher, ExampleData
from openbb_core.app.service.user_service import UserService
import requests


test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)

@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [
            ("User-Agent", None),
            ("api_key", "MOCK_API_KEY"),
            ("x-api-token", "MOCK_API_KEY"),
        ],
        "filter_query_parameters": [
            ("api_key", "MOCK_API_KEY"),
            ("x-api-token", "MOCK_API_KEY"),
        ],
    }

#
def test_ExampleFetcher(credentials=test_credentials):
    params = {"symbol": "AAPL", "limit": 5, "use_cache": False}
    fetcher = ExampleFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

def test_ExampleFetcherNoLimit(credentials=test_credentials):
    params = {"symbol": "AAPL",  "use_cache": False}
    fetcher = ExampleFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

@pytest.mark.record_http
def test_fetch_http_data(credentials=test_credentials):
    params = {"symbol": "AAPL",  "use_cache": False}
    fetcher = ExampleFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

def test_ExampleData():

    test_dict = {'symbol': 'AAPL', 'date': '2024-02-27', 'marketCap': 2844761945830}

    ed = ExampleData(**test_dict)

    print(f'{ed.marketCap}')







