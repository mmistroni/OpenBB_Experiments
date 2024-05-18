# OpenBB CFTC Provider

This module contains an extension to OBB FMP Providr that exposes FMP Commitment of Traders data. 

It will allow you to
- Get all Commitment of traders contracts via route obb.mmcftc.cot_list
- Get commitment of traders for particular contract via route obb.mmcftc.cot(symbol='VX')

To Run tests for this project you will need to install the packages beow
- pytest-vcr
- pytest-http
- wrapt
- aiohttp_client_cache


There is an helper function you can leverage to check what the endpoint will return

>>> from openbb_providers.utils.helpers import get_commitment_of_traders
>>> get_commitment_of_traders(symbol='VX')

To install this from source , you will need to launch pip install -e . from top directory (openbb_mmprvds)
