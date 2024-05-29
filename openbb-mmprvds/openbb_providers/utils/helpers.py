"""Pyth2 Provider Helpers"""


from openbb_providers.models.cftc import CommitmentOfTradersAnalysisFetcher
from openbb_providers.models.cftc_contracts import CommitmentOfTradersReportFetcher
from openbb_providers.models.cramer import CramerFetcher
import random
import logging
import asyncio
from openbb_core.app.service.user_service import UserService



def get_cftc_contracts():
    credentials = UserService().default_user_settings.credentials.model_dump(
        mode="json"
    )
    fetcher = CommitmentOfTradersReportFetcher()
    res = fetcher.fetch_data({}, credentials)
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(asyncio.gather(*[res]))
    logging.info(f'Obtained:{data}')
    return data

def get_commitment_of_traders(symbol:str):
    credentials = UserService().default_user_settings.credentials.model_dump(
        mode="json"
    )
    fetcher = CommitmentOfTradersAnalysisFetcher()
    params = {'symbol' : 'VX'}
    res = fetcher.fetch_data(params, credentials)
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(asyncio.gather(*[res]))
    logging.info(f'Obtained:{data}')
    return data

def get_cramer():
    credentials = UserService().default_user_settings.credentials.model_dump(
        mode="json"
    )
    fetcher =CramerFetcher()
    params = {'lookback' : 10}
    res = fetcher.fetch_data(params, credentials)
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(asyncio.gather(*[res]))
    logging.info(f'Obtained:{data}')
    return data






