"""Pyth Provider Module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_providers.models.fetchers import ExampleFetcher
from openbb_providers.models.cftc import CommitmentOfTradersFetcher
from openbb_providers.models.cftc_contracts import  CFTCContractsFetcher
cftc_provider = Provider(
    name="cftc",
    website="https://pyth.network/",
    description=(
        "Pyth2's complete suite of APIs solves all your market data needs. From contracts to frontend, Pyth has it covered."
        +" No subscription necessary: read the docs and connect instantly!"
    ),
    credentials=["api_key"],
    fetcher_dict={
        "CFTCContracts"  :  CFTCContractsFetcher,
        'CommitmentOfTraders' : CommitmentOfTradersFetcher
    },
)
