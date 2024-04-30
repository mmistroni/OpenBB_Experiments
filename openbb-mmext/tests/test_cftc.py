
import pytest
from openbb_mmext.models.cftc import CommitmentOfTradersData, CommitmentOfTradersFetcher
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

def test_cftc_data():

    test_dict = {'symbol': 'VX', 'date': '2024-01-30 00:00:00', 'name': 'S&P 500 VIX (VI)',
                 'sector': 'INDICES', 'exchange': 'MICRO E-MINI S&P 500 INDEX - CHICAGO MERCANTILE EXCHANGE',
                 'currentLongMarketSituation': 58.47, 'currentShortMarketSituation': 41.53,
                 'marketSituation': 'Bullish',
                 'previousLongMarketSituation': 65.97, 'previousShortMarketSituation': 34.03,
                 'previousMarketSituation': 'Bullish', 'netPostion': 19315, 'previousNetPosition': 35733,
                 'changeInNetPosition': -45.95, 'marketSentiment': 'Increasing Bearish', 'reversalTrend': False}

    ed = CommitmentOfTradersData(**test_dict)

    assert ed.symbol == 'VX'
    assert ed.date == '2024-01-30 00:00:00'
    assert ed.name == 'S&P 500 VIX (VI)'
    assert ed.current_long_market_situation == 58.47
    assert ed.current_short_market_situation == 41.53
    assert ed.previous_long_market_situation == 65.97
    assert ed.previous_short_market_situation == 34.03
    assert ed.contract_sentiment == 'Bullish'
    assert ed.previous_contract_sentiment  == 'Bullish'
    assert ed.reversal_trend  == False


@pytest.mark.record_http
def test_fetch_http_data_cftc(credentials=test_credentials):
    params = {"symbol": "VX", "limit": 5, "use_cache": False}
    fetcher = CommitmentOfTradersFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


