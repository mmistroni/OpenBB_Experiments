from typing import Any, Dict, List, Optional
from datetime import date
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field
from openbb_providers.utils.finviz_helpers import run_screener
from pydantic import BaseModel, model_validator
from typing import Optional, List
import json

import logging

import requests


class FinvizScreenerQueryParams(QueryParams):
    """
    FMP Query Parameters for finviz screener

    https://pypi.org/project/finvizfinance/

    """

    filters: Dict[str, str] = Field(description="A dictionary of Finviz Filters.")

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class FinvizScreenerData(Data):
    """Sample provider data for finviz screener.

    """

    ticker: str = Field(description="Ticker.", alias='Ticker')
    company: str = Field(description="Company Name.", alias='Company')
    sector: str = Field(description="Company Sector.", alias='Sector')
    industry : str  = Field(description="Company Industry.", alias="Industry")
    country  : str  = Field(description="Company Country", alias="Country")
    marketcap: float = Field(description="Company Market Cap.", alias="Market Cap")
    pe: float = Field(description="P/E Ratio.", alias="P/E")
    price: float = Field(description="Current Price", alias="Price")
    change: float = Field(description="Price Change", alias="Change")
    volume: float = Field(description="Volume", alias="Volume")



class FinvizScreenerFetcher(
    Fetcher[
        FinvizScreenerQueryParams,
        List[FinvizScreenerData],
    ]
):
    """ Finviz Screener Fetcher class.

    This class is responsible for the actual data retrieval.
    """


    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FinvizScreenerQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return FinvizScreenerQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FinvizScreenerQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        """
        filters = query.filters
        return run_screener(filters)

    @staticmethod
    def transform_data(
        query: FinvizScreenerQueryParams, data: List[dict], **kwargs: Any
    ) -> List[FinvizScreenerData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [FinvizScreenerData(**d) for d in data]




class FinvizWatchlistQueryParams(QueryParams):
    """
    Finviz Query Paramms for a generic watchlist

    https://pypi.org/project/finvizfinance/

    """

class FinvizWatchlistFetcher(
    Fetcher[
        FinvizWatchlistQueryParams,
        List[FinvizScreenerData],
    ]
):
    """ Finviz Screener Fetcher class.

    This class is responsible for the actual data retrieval.
    """


    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FinvizWatchlistQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return FinvizWatchlistQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FinvizWatchlistQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        Note, we are filtering on sto
        """
        price_filters = {
            'Price' : 'Over $10',
            '20-Day Simple Moving Average' : 'Price above SMA20',
            '50-Day Simple Moving Average' : 'Price above SMA50',
            '200-Day Simple Moving Average' : 'Price above SMA200',
        }

        desc_filters = {
            'Market Cap.' : '+Mid (over $2bln)',
            'Average Volume' : 'Over 200K',
        }

        fund_filters = {
            'EPS growththis year' : 'Over 20%',
            'EPS growthnext year' : 'Over 20%',
            'EPS growthqtr over qtr' : 'Over 20%',
            'Sales growthqtr over qtr' : 'Over 20%',
            'Gross Margin' : 'Over 20%',
            'Return on Equity' : 'Over +20%',
            'InstitutionalOwnership' : 'Under 60%'
        }

        filters_dict = price_filters
        filters_dict.update(desc_filters)
        filters_dict.update(fund_filters)

        return run_screener(filters_dict)

    @staticmethod
    def transform_data(
        query: FinvizWatchlistQueryParams, data: List[dict], **kwargs: Any
    ) -> List[FinvizScreenerData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [FinvizScreenerData(**d) for d in data]



class FinvizHiLoQueryParams(QueryParams):
    """
    Finviz Query Paramms for a generic watchlist

    https://pypi.org/project/finvizfinance/

    """

class FinvizHiLoData(Data):
    """Sample provider data for finviz screener.

    """

    new_high: List[str] = Field(description="Ticker of stocks that reached new highs.")
    new_low: List[str] =  Field(description="Ticker of stocks that reached new low.")
    strength: int = Field(description="This shows the number of stocks on the NYSE at 52-week highs compared to those at 52-week lows", alias='Sector')


class FinvizHiLoFetcher(
    Fetcher[
        FinvizHiLoQueryParams,
        List[FinvizHiLoData],
    ]
):
    """ Finviz Screener Fetcher class. for highlow

    This class is responsible for the actual data retrieval.
    """


    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FinvizHiLoQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return FinvizHiLoQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FinvizHiLoQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        """

        high_filter = 'New High'
        low_filter = 'New Low'

        high_filter_dict = {'52-Week High/Low': high_filter}
        low_filter_dict = {'52-Week High/Low': low_filter}

        highs = run_screener(high_filter_dict)
        high_ticks = [d['Ticker'] for d in highs]
        lows = run_screener(low_filter_dict)
        low_ticks = [d['Ticker'] for d in lows]

        return [dict(new_high=high_ticks, new_low=low_ticks, strength=len(high_ticks) - len(low_ticks))]

    @staticmethod
    def transform_data(
        query: FinvizHiLoQueryParams, data: List[dict], **kwargs: Any
    ) -> List[FinvizHiLoData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [FinvizHiLoData(**d) for d in data]

