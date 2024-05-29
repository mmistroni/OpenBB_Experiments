from typing import Any, Dict, List, Optional
from datetime import date
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_fmp.models.etf_info import FMPEtfInfoFetcher
from pydantic import Field
import logging

import requests


class FMPMarketCapQueryParams(QueryParams):
    """
    FMP  Parameters for Company MarketCap

    https://site.financialmodelingprep.com/developer/docs#market-cap-company-information

    """

    symbol: str = Field(description="Symbol to query.")
    limit: Optional[int] = Field(description="Number of days of marketcap", default=220)


class FMPMarketCapData(Data):
    """Sample provider data for commitment of traders.

    """

    symbol: str = Field(description="Ticker.")
    date: str = Field(description="As Of Date.")
    marketcap: float = Field(description="Market Cap.", alias="marketCap")


class FMPMarketCapDataFetcher(
    Fetcher[
        FMPMarketCapQueryParams,
        List[FMPMarketCapData],
    ]
):
    """ FMP Commitment of Traders Fetcher class.

    This class is responsible for the actual data retrieval.
    """
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPMarketCapQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return FMPMarketCapQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPMarketCapQueryParams,
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
        limit = query.limit or 220

        base_url = f'https://financialmodelingprep.com/api/v3/historical-market-capitalization/AAPL?limit={limit}&apikey={api_key}'

        logging.info(f'Calling url:{base_url}')

        example_response = requests.get(base_url).json()

        if 'Error Message' in example_response:
            raise Exception(example_response['Error Message'])

        return example_response[0:limit]

    @staticmethod
    def transform_data(
        query: FMPMarketCapQueryParams, data: List[dict], **kwargs: Any
    ) -> List[FMPMarketCapData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [FMPMarketCapData(**d) for d in data]
