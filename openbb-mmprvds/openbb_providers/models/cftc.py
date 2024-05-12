from typing import Any, Dict, List, Optional
from datetime import date
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_fmp.models.etf_info import FMPEtfInfoFetcher
from pydantic import Field
import logging

import requests


class CommitmentOfTradersAnalysisQueryParams(QueryParams):
    """
    FMP Query Parameters for commitment of traders analysis

    https://site.financialmodelingprep.com/developer/docs/analysis-by-symbol-commitment-of-traders

    """

    symbol: str = Field(description="Symbol to query.")
    limit: Optional[int] = Field(description="Number of commitment of traders to download", default=1)


class CommitmentOfTradersAnalysisData(Data):
    """Sample provider data for commitment of traders.

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


class CommitmentOfTradersAnalysisFetcher(
    Fetcher[
        CommitmentOfTradersAnalysisQueryParams,
        List[CommitmentOfTradersAnalysisData],
    ]
):
    """ FMP Commitment of Traders Fetcher class.

    This class is responsible for the actual data retrieval.
    """
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CommitmentOfTradersAnalysisQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return CommitmentOfTradersAnalysisQueryParams(**params)

    @staticmethod
    def extract_data(
        query: CommitmentOfTradersAnalysisQueryParams,
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

        logging.info(f'Calling url:{base_url}')

        example_response = requests.get(base_url).json()

        if 'Error Message' in example_response:
            raise Exception(example_response['Error Message'])

        return example_response[0:limit]

    @staticmethod
    def transform_data(
        query: CommitmentOfTradersAnalysisQueryParams, data: List[dict], **kwargs: Any
    ) -> List[CommitmentOfTradersAnalysisData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [CommitmentOfTradersAnalysisData(**d) for d in data]
