# OpenBB CFTC Provider

pytest-vcr
pytest-http
wrapt
aiohttp_client_cache


This extension integrates the CFTC data provider to extract commitment of traders

the provider can be ran manually using openbb_providers's helper module like this

>>> from openbb_providers.utils.helpers import get_commitment_of_traders
>>> get_commitment_of_traders(symbol='VX')


