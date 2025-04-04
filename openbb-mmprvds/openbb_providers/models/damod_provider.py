from typing import Any, Dict, List, Optional
from datetime import date
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field
from openbb_providers.utils.finviz_helpers import run_screener
from pydantic import BaseModel, model_validator
from typing import Optional, List
from openbb_providers.utils.damod_utils import get_betas, get_fgrowtheps, get_pe,\
                              get_ps, get_pvdata, get_roe, get_valuation_metrics
import json

import logging

import requests


class RoeQueryParams(QueryParams):
    """
    Query Parameters for ADamodaran finviz screener

    https://pypi.org/project/finvizfinance/

    """

class RoeData(Data):
    """Sample provider damod roe data.
		
    """
    industry_name: str = Field(description="Industry Name", alias='Industry Name')
    number_of_firms: int = Field(description="Number of Firms.", alias='Number of firms')
    roe: float = Field(description="ROE unadjusted", alias='ROE')
    


class RoeFetcher(
    Fetcher[
        RoeQueryParams,
        List[RoeData],
    ]
):
    """ Finviz Screener Fetcher class.

    This class is responsible for the actual data retrieval.
    """


    @staticmethod
    def transform_query(params: Dict[str, Any]) -> RoeQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return RoeQueryParams(**params)

    @staticmethod
    def extract_data(
        query: RoeQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        """
        roe_df =  get_roe()
        return roe_df.to_dict('records')

    @staticmethod
    def transform_data(
        query: RoeQueryParams, data: List[dict], **kwargs: Any
    ) -> List[RoeData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [RoeData(**d) for d in data]


class IndustryValuationQueryParams(QueryParams):
    """
    Query Parameters for ADamodaran data

    """


class IndustryValuationData(Data):
    """Sample provider damod roe data.

    """
    industry_name: str = Field(description="Industry Name", alias='Industry Name')
    number_of_firms: int = Field(description="Number of Firms.", alias='Number of firms')
    roe: float = Field(description="ROE unadjusted", alias='ROE')
    fundamental_growth: float = Field(description="Industry Fundamental Growth", alias='Fundamental Growth')
    current_pe: float = Field(description="Industry Current PE", alias='Current PE')
    trailing_pe: float = Field(description="Industry Fundamental Growth", alias='Trailing PE')
    forward_pe: float = Field(description="Industry Fundamental Growth", alias='Forward PE')
    expected_growth_5y: float = Field(description="Industry Fundamental Growth", alias='Expected Growth - next 5 years')
    peg: float = Field(description="Industry Fundamental Growth", alias='PEG Ratio')
    pbv: float = Field(description="Industry Fundamental Growth", alias='PBV',)
    ev_invested_capital: float = Field(description="Industry Fundamental Growth", alias='EV/Invested Capital')
    roic: float = Field(description="Industry Fundamental Growth", alias='ROIC')
    ceo_holdings: float = Field(description="Industry Fundamental Growth", alias='CEO Holdings',)
    corporate_holdings: float = Field(description="Industry Fundamental Growth", alias='Corporate Holdings')
    institutional_holdings: float = Field(description="Industry Fundamental Growth", alias='Insitutional Holdings')
    insider_holdings: float = Field(description="Industry Fundamental Growth", alias='Insider Holdings')

class IndustryValuationFetcher(
    Fetcher[
        IndustryValuationQueryParams,
        List[IndustryValuationData],
    ]
):
    """ Finviz Screener Fetcher class.

    This class is responsible for the actual data retrieval.
    """

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> IndustryValuationQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return IndustryValuationQueryParams(**params)

    @staticmethod
    def extract_data(
            query: IndustryValuationQueryParams,
            credentials: Optional[Dict[str, str]],
            **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        """
        metrics_df = get_valuation_metrics()
        return metrics_df.to_dict('records')

    @staticmethod
    def transform_data(
            query: IndustryValuationQueryParams, data: List[dict], **kwargs: Any
    ) -> List[RoeData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [IndustryValuationData(**d) for d in data]






