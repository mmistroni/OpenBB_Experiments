"""Pyth Provider Module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_mm.models.fetchers import ExampleFetcher
mm_provider = Provider(
    name="mm",
    website="https://pyth.network/",
    description=(
        "MM Sample Provider.complete suite of APIs solves all your market data needs. From contracts to frontend, Pyth has it covered."
        +" No subscription necessary: read the docs and connect instantly!"
    ),
    fetcher_dict={
        "Example" : ExampleFetcher
    },
)
