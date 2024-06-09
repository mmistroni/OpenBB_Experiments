from typing import Any, Dict, List, Optional
from datetime import date
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_providers.utils.seekingalpha_helpers import get_seekingalpha_dividend_picks, get_seekingalpha_stock_ideas
from pydantic import Field
import logging

import requests


class SeekingAlphaQueryParams(QueryParams):
    """
    Seeking Alpha Query Parameters


    """


class SeekingAlphaData(Data):
    """Sample data class for SeekingAlpha data.

    """

    tickers: str = Field(description="Ticker mentioned in article.")
    as_of_date: date = Field(description="As Of Date of the feed.")
    detail: str = Field(description="Details of Article")
    link: str = Field(description="Link to Article")



class SAStockIdeaFetcher(
    Fetcher[
        SeekingAlphaQueryParams,
        List[SeekingAlphaData],
    ]
):
    """ SA Fetcher class.

    This class is responsible for the actual data retrieval.
    """
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> SeekingAlphaQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return SeekingAlphaQueryParams(**params)

    @staticmethod
    def extract_data(
        query: SeekingAlphaQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        """
        example_response = get_seekingalpha_stock_ideas()

        if 'Error Message' in example_response:
            raise Exception(example_response['Error Message'])

        return example_response

    @staticmethod
    def transform_data(
        query: SeekingAlphaQueryParams, data: List[dict], **kwargs: Any
    ) -> List[SeekingAlphaData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [SeekingAlphaData(**d) for d in data]

class SADividendPicksFetcher(
    Fetcher[
        SeekingAlphaQueryParams,
        List[SeekingAlphaData],
    ]
):
    """ SA Dividend Picks

    This class is responsible for the actual data retrieval.
    """
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> SeekingAlphaQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return SeekingAlphaQueryParams(**params)

    @staticmethod
    def extract_data(
        query: SeekingAlphaQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        """
        example_response = get_seekingalpha_dividend_picks()

        if 'Error Message' in example_response:
            raise Exception(example_response['Error Message'])

        return example_response

    @staticmethod
    def transform_data(
        query: SeekingAlphaQueryParams, data: List[dict], **kwargs: Any
    ) -> List[SeekingAlphaData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [SeekingAlphaData(**d) for d in data]


