from typing import Any, Dict, List, Optional
from datetime import date
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field

import requests


class CFTCContractsQueryParams(QueryParams):
    """Example provider query.

    This is the definition of our query parameters that are specific to this provider.
    We use this class to create our own parameters that will provided as input to the
    command.
    """

class CFTCContractsData(Data):
    """Sample provider data.

    The fields are displayed as-is in the output of the command. In this case, its the
    symbol, date and marketCap.
    """

    symbol: str = Field(description="Contract symbol.", alias="trading_symbol")
    short_name: str = Field(description="Contract s hort name.")


class CFTCContractsFetcher(
    Fetcher[
        CFTCContractsQueryParams,
        List[CFTCContractsData],
    ]
):
    """Example Fetcher class.

    This class is responsible for the actual data retrieval.
    """

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CFTCContractsQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return CFTCContractsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: CFTCContractsQueryParams,
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

        base_url = f'https://financialmodelingprep.com/api/v4/commitment_of_traders_report/list?apikey={api_key}'

        # Here we mock an example_response for brevity.
        example_response = requests.get(base_url).json()

        return example_response

    @staticmethod
    def transform_data(
        query: CFTCContractsQueryParams, data: List[dict], **kwargs: Any
    ) -> List[CFTCContractsData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [CFTCContractsData(**d) for d in data]
