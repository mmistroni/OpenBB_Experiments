"""Pyth2 Provider Helpers"""

from openbb_providers.models.fetchers import ExampleFetcher
from openbb_providers.models.cftc import CommitmentOfTradersFetcher
from openbb_providers.models.cftc_contracts import CFTCContractsFetcher
from openbb import obb

import logging
import asyncio
from openbb_core.app.service.user_service import UserService



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

def call_providers():
    print(obb.mmcftc.cot2(symbol='VX'))