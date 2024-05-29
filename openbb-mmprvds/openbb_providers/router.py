import requests
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (ExtraParams, ProviderChoices,
                                                StandardParams)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel
from openbb_core.app.model.example import APIEx, PythonEx

router = Router(prefix="")



@router.command(
    model="CommitmentOfTradersReport",
    examples = [
        APIEx(
            description="Return all Commitment of traders contracts",
            parameters={})
    ]
)
async def cot_list(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))

@router.command(
    model="CommitmentOfTradersAnalysis",
    examples=[
        APIEx(
            description="Get commitment of traders analysis for a specific contract(VX), returning the last analysis.",
            parameters={"symbol": "VX"}),

        APIEx(
            description="Get commitment of traders analysis for VX, returning last 100 results.",
            parameters={"symbol" : "VX", "limit": 100})
    ]
)
async def cot(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))

@router.command(
    model="FMPMarketCapDataFetcher",
    examples=[
        APIEx(
            description="Return daily marketcap for last 220 days.",
            parameters={"symbol": "AAPL"}),

        APIEx(
            description="Return daily marketcap for the number of days specified by the limit parameters.",
            parameters={"symbol" : "AAPL", "limit": 100})
    ]

)
async def marketcap(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))

@router.command(model="SeekingAlphaDividendPicks")
async def sa_dividend_picks(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))

@router.command(model="SeekingAlphaStockIdeas")
async def sa_stock_ideas(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))


@router.command(model="SeekingAlphaStockIdeas")
async def cramer(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))







