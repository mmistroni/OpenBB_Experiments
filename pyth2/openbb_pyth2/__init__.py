"""Pyth Provider Module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_pyth2.models.fetchers import ExampleFetcher
pyth2_provider = Provider(
    name="pyth2",
    website="https://pyth.network/",
    description=(
        "Pyth2's complete suite of APIs solves all your market data needs. From contracts to frontend, Pyth has it covered."
        +" No subscription necessary: read the docs and connect instantly!"
    ),
    fetcher_dict={
        "Example" : ExampleFetcher
    },
)