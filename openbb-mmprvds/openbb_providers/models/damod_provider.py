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
                              get_ps, get_pvdata, get_roe
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
    roe_unadjusted: str = Field(description="ROE unadjusted", alias='ROE (adjusted for R&D)')
    roe_adjusted_rd : str  = Field(description="ROE adjusted for r & d.", alias="Industry")
    


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
        return get_roe()

    @staticmethod
    def transform_data(
        query: RoeQueryParams, data: List[dict], **kwargs: Any
    ) -> List[RoeData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [RoeData(**d) for d in data]


