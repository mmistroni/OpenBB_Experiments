from typing import Any, Dict, List, Optional
from datetime import date
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_providers.utils.finviz_helpers import run_screener
from pydantic import Field
import logging

import requests


class FinvizCanslimQueryParams(QueryParams):
    """
    Query Parameters for Canlsim Stocks
    https://finviz.com/screener.ashx
    For Finviz screener, all query parameters are provided via filters.
    See FivizCanslimFetcher
    """


class FinvizData(Data):
    """
        holder of data returned by finviz screener

    """

    ticker: str = Field(description="Ticker.", alias='Ticker')
    company: str = Field(description="Company Name.", alias='Company')
    sector: str = Field(description="Sector", alias='Sector')
    industry: str = Field(description="Industry.", alias='Industry')
    country: str = Field(description="Country.", alias='Country')
    marketcap: float = Field(description="Market Cap", alias='Market Cap')
    peratio:float = Field(description='P/E Ratio', alias='P/E')
    price: float = Field(description="Price.", alias='Price')
    change: float = Field(description="Change.", alias='Change')
    volume: float = Field(description="Volume", alias='Volume')


class FinvizCanslimFetcher(
    Fetcher[
        FinvizCanslimQueryParams,
        List[FinvizData],
    ]
):
    """ Finviz Canslim Fetcher.
        Fetches stocsk from Finviz which follow these criteria
        def  get_canslim():
    '''
    Descriptive Parameters:

    Average Volume: Over 200K
    Float: Under 50M
    Stocks only (ex-Funds)
    Stocks that have above 200K average daily volume are liquid and stocks with a low float under 50 million shares are
        more likely to explode faster because of the lower supply.
        For example, low float stocks like FUTU, CELH, BLNK, GRWG, SI, and DQ are all up more than 750% from their 52-week lows.

    Fundamental Parameters:

    EPS Growth This Year: Over 20%
    EPS Growth Next Year: Over 20%
    EPS Growth qtr over qtr: Over 20%
    Sales Growth qtr over qtr: Over 20%
    EPS Growth past 5 years: Over 20%
    Return on Equity: Positive (>0%)
    Gross Margin: Positive (>0%)
    Institutional Sponsorship: Over 20%

    Technical Parameters:

    Price above SMA20
    Price above SMA50
    Price above SMA200
    0–10% below High


    This class is responsible for the actual data retrieval.
    """
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FinvizCanslimQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return FinvizCanslimQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FinvizCanslimQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        """
        ## Build filters

        price_filters = {
            '20-Day Simple Moving Average': 'Price above SMA20',
            '50-Day Simple Moving Average': 'Price above SMA50',
            '200-Day Simple Moving Average': 'Price above SMA200',
            '52-Week High/Low': '0-10% below High'
        }

        desc_filters = {
            'Average Volume': 'Over 200K',
            'Float': 'Under 50M',
        }

        fund_filters = {
            'Average Volume': 'Over 200K',
            'Float': 'Under 50M',
            'EPS growththis year': 'Over 20%',
            'EPS growthnext year': 'Over 20%',
            'EPS growthqtr over qtr': 'Over 20%',
            'Sales growthqtr over qtr': 'Over 20%',
            'EPS growthpast 5 years': 'Over 20%',
            'Gross Margin': 'Positive (>0%)',
            'Return on Equity': 'Positive (>0%)',
            'InstitutionalOwnership': 'Over 20%'
        }
        filters_dict = price_filters
        filters_dict.update(desc_filters)
        filters_dict.update(fund_filters)

        example_response = run_screener(filters_dict)
        if 'Error Message' in example_response:
            raise Exception(example_response['Error Message'])
        return example_response

    @staticmethod
    def transform_data(
        query: FinvizCanslimQueryParams, data: List[dict], **kwargs: Any
    ) -> List[FinvizData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [FinvizData(**d) for d in data]
