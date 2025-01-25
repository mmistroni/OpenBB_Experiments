from typing import Any, Dict, List, Optional
from datetime import date
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_providers.utils.quiverquants_utils import get_government_contracts
from pydantic import Field

class GovernmentContractsQueryParams(QueryParams):
    """
    Governnment Contracts Query Parameters


    """
    

class GovernmentContractsData(Data):
    """Sample data for quiverquants government contracts data.

    """

    ticker: str = Field(description="Ticker .")
    asofdate: str = Field(description="as of date.", alias='asofdate')
    amount: str = Field(description="contract amount")
    funding_agency:str = Field(description="funding agency")
    description:str = Field(description="contract description")


class GovernmentContractsFetcher(
    Fetcher[
        GovernmentContractsQueryParams,
        List[GovernmentContractsData],
    ]
):
    """ Government contracts fetcher.
    """
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> GovernmentContractsQueryParams:
        """Define example transform_query.

        Here we can pre-process the query parameters and add any extra parameters that
        will be used inside the extract_data method.
        """
        return GovernmentContractsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: GovernmentContractsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[dict]:
        """Define example extract_data.

        Here we make the actual request to the data provider and receive the raw data.
        If you said your Provider class needs credentials you can get them here.
        """

        try:
            response = get_government_contracts()

            return response.to_dict('records')
        except Exception as e:
            raise Exception(str(e))

    @staticmethod
    def transform_data(
        query: GovernmentContractsQueryParams, data: List[dict], **kwargs: Any
    ) -> List[GovernmentContractsData]:
        """Define example transform_data.

        Right now, we're converting the data to fit our desired format.
        You can apply other transformations to it here.
        """
        return [GovernmentContractsData(**d) for d in data]

