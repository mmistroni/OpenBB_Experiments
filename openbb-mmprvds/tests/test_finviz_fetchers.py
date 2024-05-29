"""Pyth2 Fetchers tests."""
import pytest
from openbb_providers.models.finviz import FinvizData, FinvizCanslimFetcher
from openbb_core.app.service.user_service import UserService
import re

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
def test_canslim_fetcher(credentials=test_credentials):
    params = {}
    fetcher = FinvizCanslimFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


