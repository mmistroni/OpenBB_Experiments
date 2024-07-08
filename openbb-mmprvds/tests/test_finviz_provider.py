"""Pyth2 Fetchers tests."""
import pytest
from openbb_providers.models.finviz_provider import FinvizScreenerData, FinvizScreenerQueryParams, FinvizScreenerFetcher,\
                                                    FinvizWatchlistFetcher
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
def test_finviz_fetcher(credentials=test_credentials):
    generic_filter_lst = ['Market Cap.=+Small (over $300mln)',
                    'Average Volume=Over 200K',
                    'Price=Over $10',
                    'EPS growththis year=Over 20%',
                    'EPS growthnext year=Positive (>0%)',
                    'Gross Margin=Positive (>0%)',
                    'EPS growthqtr over qtr=Over 20%',
                    'Sales growthqtr over qtr=Over 20%',
                    'Return on Equity=Positive (>0%)'
                    ]

    params = {'filters' : generic_filter_lst}
    fetcher = FinvizScreenerFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

@pytest.mark.record_http
def test_finviz_watchilst_fetcher(credentials=test_credentials):
    params = {}
    fetcher = FinvizWatchlistFetcher()
    result = fetcher.test(params, credentials)
    assert result is None



def test_finviz_data():

    finviz_test_dict = {'Ticker': 'ANF', 'Company': 'Abercrombie & Fitch Co.',
                          'Sector': 'Consumer Cyclical', 'Industry': 'Apparel Retail',
                          'Country': 'USA', 'Market Cap': 8920000000.0, 'P/E': 21.71, 'Price': 174.5, 'Change': -0.006, 'Volume': 1725757.0}

    mc = FinvizScreenerData(**finviz_test_dict)

    assert mc.ticker == finviz_test_dict['Ticker']
    assert mc.company == finviz_test_dict['Company']
    assert mc.sector == finviz_test_dict['Sector']
    assert mc.industry == finviz_test_dict['Industry']
    assert mc.country == finviz_test_dict['Country']
    assert mc.marketcap == finviz_test_dict['Market Cap']
    assert mc.pe == finviz_test_dict['P/E']
    assert mc.price == finviz_test_dict['Price']
    assert mc.change == finviz_test_dict['Change']


## Add test for HiLo
