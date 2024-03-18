"""Pyth2 Fetchers tests."""
import pytest
from openbb_pyth2.models.cftc_contracts import CFTCContractsData, CFTCContractsFetcher
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
@pytest.mark.integration
def test_cftc_fetcher(credentials=test_credentials):
    params = { "use_cache": False}
    fetcher = CFTCContractsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

def test_cftc_data():

    test_dict = {
                    "trading_symbol": "NG",
                    "short_name": "Natural Gas (NG)"
    }

    cdata = CFTCContractsData(**test_dict)

    assert cdata.symbol == 'NG'
    assert cdata.short_name == "Natural Gas (NG)"

@pytest.mark.record_http
def test_fetch_http_data_cftc_contracts(credentials=test_credentials):
    params = {"symbol": "VX", "limit": 5, "use_cache": False}
    fetcher = CFTCContractsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None




