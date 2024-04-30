from typing import Any, Dict, List, Optional
from datetime import date
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field

import requests


class CommitmentOfTradersQueryParams(QueryParams):
    """Example provider query.

    This is the definition of our query parameters that are specific to this provider.
    We use this class to create our own parameters that will provided as input to the
    command.
    """

    symbol: str = Field(description="Symbol to query.")
    limit: Optional[int] = Field(description="Number of commitment of traders to download", default=1)


class CommitmentOfTradersData(Data):
    """Sample provider data for fething Commitment of traders data.

    The fields are displayed as-is in the output of the command. In this case, its the
    symbol, date and marketCap.
    """

    symbol: str = Field(description="Ticker.")
    date: str = Field(description="As Of Date.")
    name: str = Field(description="Name of Future.")
    current_long_market_situation : float = Field(description="Current Week Long Contracts.", alias="currentLongMarketSituation")
    current_short_market_situation: float = Field(description="Current Week Short Contracts.", alias="currentShortMarketSituation")
    previous_long_market_situation: float = Field(description="Previous Week Long Contracts.", alias="previousLongMarketSituation")
    previous_short_market_situation: float = Field(description="Previous Week Short Contracts.", alias="previousShortMarketSituation")
    contract_sentiment: str = Field(description="Current Market Sentiment for the Contract", alias="marketSituation")
    previous_contract_sentiment: str = Field(description="Previous Market Sentiment for the Contract", alias="previousMarketSituation")
    reversal_trend: bool = Field(description="flag indicating if there is a trend reversal in this contract", alias="reversalTrend")


class CommitmentOfTradersFetcher(
    Fetcher[
        CommitmentOfTradersQueryParams,
        List[CommitmentOfTradersData],
    ]
):
    """Example Fetcher class.

    This class is responsible for the actual data retrieval.
    """

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CommitmentOfTradersQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return CommitmentOfTradersQueryParams(**params)

    @staticmethod
    def extract_data(
        query: CommitmentOfTradersQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        """
        api_key = (
            credentials.get("fmp_api_key")
            if credentials
            else ""
        )

        symbol = query.symbol
        limit = query.limit or 1

        base_url = f'https://financialmodelingprep.com/api/v4/commitment_of_traders_report_analysis/{symbol}?apikey={api_key}'

        # Here we mock an example_response for brevity.
        example_response = requests.get(base_url).json()[0:limit]

        return example_response

    @staticmethod
    def transform_data(
        query: CommitmentOfTradersQueryParams, data: List[dict], **kwargs: Any
    ) -> List[CommitmentOfTradersData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [CommitmentOfTradersData(**d) for d in data]
