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
        PythonEx(
            description="Return all Commitment of traders contracts",
            code=[
            "cot_report = obb.mmext.cot_list()"
                ]
        )
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
        PythonEx(
            description="Return commitment of traders analysis for a specific symbol",
            code=[
            "vx = obb.mmext.cot(symbol='VX')",
            "vx = obb.mmext.cot(symbol='VX', limit=10)",
                ]
        )
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
        PythonEx(
                    description="Return MarketCap for a company (default last 220 days)",
                    code=[
                    "mkcap = obb.mmext.marketcap(symbol='T')",
                    "mkcap = obb.mmext.marketcap(symbol='T', limit=100)"
                        ]
        )

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

@router.command(
        model="SeekingAlphaDividendPicks",
        examples=[
                PythonEx(
                            description="Return SeekingAlpha dividend picsk article)",
                            code=[
                            "obb.mmext.sa_dividend_picks()"
                                ]
                )

            ]
)
async def sa_dividend_picks(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))

@router.command(
    model="SeekingAlphaStockIdeas",
    examples = [
        PythonEx(
            description="Return SeekingAlpha stock ideas articles)",
            code=[
                "obb.mmext.sa_stock_ideas()"
            ]
        )
    ]
)
async def sa_stock_ideas(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CramerRecommendations",
    examples = [
            PythonEx(
                description="Return Jim Cramer stock recommendations)",
                code=[
                    "obb.mmext.cramer()"
                ]
            )
        ]
)

async def cramer(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="GovernmentContracts",
    examples = [
            PythonEx(
                description="Return Government Contracts from QuiverQuants)",
                code=[
                    "obb.mmext.gov_contracts()"
                ]
            )
        ]
)

async def gov_contracts(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))

@router.command(
    model="IndustryRoe",
    examples = [
            PythonEx(
                description="Return Industry Roes from ADamodaran website)",
                code=[
                    "obb.mmext.industry_roe()"
                ]
            )
        ]
)

async def industry_roe(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))


