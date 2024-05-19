import requests
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (ExtraParams, ProviderChoices,
                                                StandardParams)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel
from openbb_providers.utils.seekingalpha_helpers import get_seekingalpha_dividend_picks, get_seekingalpha_stock_ideas

router = Router(prefix="")


@router.command(methods=["GET"])
def xot() -> OBBject[dict]:
    return OBBject(results = {'foo' : 'bar'})

@router.command(model="CommitmentOfTradersReport")
async def cot_list(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))

@router.command(model="CommitmentOfTradersAnalysis")
async def cot(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))

@router.command(methods=["GET"])
def sa_stock_ideas() -> OBBject[dict]:
    data = get_seekingalpha_stock_ideas()
    return OBBject(results = data)

@router.command(methods=["GET"])
def sa_dividend_picks() -> OBBject[dict]:
    data = get_seekingalpha_dividend_picks()
    return OBBject(results = data)

@router.command(model="FMPMarketCapDataFetcher")
async def cot(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))




