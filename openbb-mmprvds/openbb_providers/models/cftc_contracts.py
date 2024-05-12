from typing import Any, Dict, List, Optional
from datetime import date
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field

import requests


class CommitmentOfTradersReportListQueryParams(QueryParams):
    """
    Commitment of Traders report  list

    https://site.financialmodelingprep.com/developer/docs#commitment-of-traders-report-stock-list

    """

class CommitmentOfTradersReportListData(Data):
    """
    This class hold data related to commitment of traders contracts

    The fields are displayed as-is in the output of the command. In this case, its the
    symbol, date and marketCap.
    """

    symbol: str = Field(description="Contract symbol.", alias="trading_symbol")
    short_name: str = Field(description="Contract s hort name.")


class CommitmentOfTradersReportFetcher(
    Fetcher[
        CommitmentOfTradersReportListQueryParams,
        List[CommitmentOfTradersReportListData],
    ]
):
    """Example Fetcher class.

    This class is responsible for the actual data retrieval.
    """

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CommitmentOfTradersReportListQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return CommitmentOfTradersReportListQueryParams(**params)

    @staticmethod
    def extract_data(
        query: CommitmentOfTradersReportListQueryParams,
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
        query: CommitmentOfTradersReportListQueryParams, data: List[dict], **kwargs: Any
    ) -> List[CommitmentOfTradersReportListData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [CommitmentOfTradersReportListData(**d) for d in data]
