"""Pyth2 Fetchers tests."""
import pytest
from openbb_pyth2.models.fetchers import ExampleFetcher, ExampleData
from openbb_core.app.service.user_service import UserService

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)

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


@pytest.mark.record_http
def test_ExampleFetcherWithHttpData(credentials=test_credentials):
    params = {"symbol": "AAPL",  "use_cache": False}
    fetcher = ExampleFetcher()
    result = fetcher.test(params, credentials)




def test_ExampleData():

    test_dict = {'symbol': 'AAPL', 'date': '2024-02-27', 'marketCap': 2844761945830}

    ed = ExampleData(**test_dict)

    print(f'{ed.marketCap}')



