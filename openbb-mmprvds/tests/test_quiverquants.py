"""Pyth2 Fetchers tests."""
import pytest
from openbb_providers.models.quiverquants import GovernmentContractsFetcher, GovernmentContractsData, GovernmentContractsQueryParams
from openbb_core.app.service.user_service import UserService
import re
import requests
from bs4 import BeautifulSoup
from datetime import date, datetime

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


def test_government_contracts_data():

    test_dict = {'ticker': 'ANSS', 'asofdate': '2025-01-23', 
                 'amount': '$106,860', 
                 'funding_agency': 'National Aeronautics and Space Administration', 
                 'description': 'THIS BPA CALL IS TO PURCHASE ANSYS SOFTWARE PER QUOTE RN-LT-603437 DATED 01/08/2025...THE PERIOD OF PERFORMANCE IS 04/01/2025-03/31/2026.'}

    ed = GovernmentContractsData(**test_dict)

    assert ed.ticker == test_dict['ticker']
    assert ed.asofdate == test_dict['asofdate']
    assert ed.amount == test_dict['amount']
    assert ed.funding_agency == test_dict['funding_agency']
    assert ed.description == test_dict['description']
    
@pytest.mark.vcr
def test_fetch_http_data_government_contracts(credentials=test_credentials):
    params = {}
    fetcher = GovernmentContractsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

