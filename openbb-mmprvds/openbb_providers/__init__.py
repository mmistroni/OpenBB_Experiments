"""Pyth Provider Module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_providers.models.fetchers import ExampleFetcher
from openbb_providers.models.cftc import CommitmentOfTradersFetcher
from openbb_providers.models.cftc_contracts import  CFTCContractsFetcher
cftc_provider = Provider(
    name="cftc",
    website="https://pyth.network/",
    description=(
        "Provider for fetching CFTC data via FMP."
    ),
    credentials=["api_key"],
    fetcher_dict={
        "CommitmentOfTradersList"  :  CFTCContractsFetcher,
        'CommitmentOfTradersAnalysis' : CommitmentOfTradersFetcher
    },
)
