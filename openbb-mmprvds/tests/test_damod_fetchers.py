"""Pyth2 Fetchers tests."""
import pytest
from openbb_providers.models.damod_provider import RoeData, RoeFetcher, RoeQueryParams
from openbb_core.app.service.user_service import UserService
import re
from datetime import date

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
def test_damod_fetcher(credentials=test_credentials):
    params = {}
    fetcher = RoeFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

def test_roe_data():

    test_dict = {'Industry Name': 'Avertising',
                  'Number of firms': 54,
                  'ROE': 0.118527,

                 }


    cd = RoeData(**test_dict)

    assert cd.industry_name == test_dict['Industry Name']
    assert cd.number_of_firms == test_dict['Number of firms']
    assert cd.roe == test_dict['ROE']

