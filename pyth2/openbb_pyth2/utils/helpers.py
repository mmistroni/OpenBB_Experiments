"""Pyth2 Provider Helpers"""

from openbb_pyth2.models.fetchers import ExampleFetcher
from openbb_pyth2.models.cftc import CommitmentOfTradersFetcher
from openbb_pyth2.models.cftc_contracts import CFTCContractsFetcher
import logging
import asyncio
from openbb_core.app.service.user_service import UserService



def run_fetcher_for_symbol(symbol):
    logging.info(f'Querying for  {symbol}')
    credentials = UserService().default_user_settings.credentials.model_dump(
        mode="json"
    )
    params = {"symbol": symbol, "limit": 5, "use_cache": False}
    fetcher = ExampleFetcher()
    res = fetcher.fetch_data(params, credentials)
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(asyncio.gather(*[res]))
    logging.info(f'Obtained:{data}')
    return data

def get_cftc_contracts():
    credentials = UserService().default_user_settings.credentials.model_dump(
        mode="json"
    )
    fetcher = CFTCContractsFetcher()
    res = fetcher.fetch_data({}, credentials)
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(asyncio.gather(*[res]))
    logging.info(f'Obtained:{data}')
    return data

def get_commitment_of_traders(symbol):
    logging.info(f'Querying for  {symbol}')
    credentials = UserService().default_user_settings.credentials.model_dump(
        mode="json"
    )
    params = {"symbol": symbol, "limit": 5, "use_cache": False}
    fetcher = CommitmentOfTradersFetcher()
    res = fetcher.fetch_data(params, credentials)
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(asyncio.gather(*[res]))
    logging.info(f'Obtained:{data}')
    return data
