from openbb_core.provider.abstract.provider import Provider
from openbb_providers.models.cftc import CommitmentOfTradersFetcher

cftc_provider = Provider(
    name="cftc provider",
    website="https://pyth.network/",
    description=(
        "Simple Provider for fetching Commitment of Traders data"

    ),
    fetcher_dict={
        'CommitmentOfTraders' : CommitmentOfTradersFetcher
    },
)