"""Pyth Provider Module."""


from openbb_core.provider.abstract.provider import Provider
from openbb_fmp import fmp_provider
from openbb_providers.models.cftc import CommitmentOfTradersAnalysisFetcher
from openbb_providers.models.cftc_contracts import  CommitmentOfTradersReportFetcher
from openbb_providers.models.fmp_marketcap import FMPMarketCapDataFetcher
from openbb_providers.models.seekingalpha import SADividendPicksFetcher, SAStockIdeaFetcher
from openbb_providers.models.cramer import CramerFetcher
from openbb_providers.models.finviz_provider import FinvizScreenerFetcher, FinvizWatchlistFetcher,\
                                                    FinvizHiLoFetcher
from openbb_providers.models.quiverquants import GovernmentContractsFetcher
from openbb_providers.models.damod_provider import RoeFetcher


cftc_provider = Provider(
    name="cftc",
    website="https://pyth.network/",
    description=(
        "Provider for fetching CFTC data via FMP."
    ),
    fetcher_dict={}
)

sa_provider = Provider(
    name="sa_provider",
    website="https://pyth.network/",
    description=(
        "Provider for fetching Seeking Alpha data."
    ),
    fetcher_dict={
        'SeekingAlphaDividendPicks' : SADividendPicksFetcher,
        'SeekingAlphaStockIdeas' : SAStockIdeaFetcher
    }
)

cramer_provider = Provider(
    name="cramer_provider",
    website="https://pyth.network/",
    description=(
        "Provider for fetching Jim Cramer recommendations."
    ),
    fetcher_dict={
        'CramerRecommendations' : CramerFetcher,
    }
)

finviz_provider = Provider(
    name="finviz_provider",
    website="https://pyth.network/",
    description=(
        "Provider for Finviz Screener."
    ),
    fetcher_dict={
        'FinvizScreener' : FinvizScreenerFetcher,
        "FinvizWatchlist": FinvizWatchlistFetcher,
        "FinvizHiLoFetcher" : FinvizHiLoFetcher
    }
)

quiverquants_provider = Provider(
    name="quiverquants_provider",
    website="https://pyth.network/",
    description=(
        "Provider for Government Contracts."
    ),
    fetcher_dict={
        'GovernmentContracts' : GovernmentContractsFetcher
    }
)

damodaran_provider = Provider(
    name="damodaran_provider",
    website="https://pyth.network/",
    description=(
        "Provider for ADamodaran valuations."
    ),
    fetcher_dict={
        'IndustryRoe' : RoeFetcher
    }
)



fmp_provider.fetcher_dict.update({
        "CommitmentOfTradersAnalysis": CommitmentOfTradersAnalysisFetcher,
        "CommitmentOfTradersReport": CommitmentOfTradersReportFetcher,
        "FMPMarketCapDataFetcher" : FMPMarketCapDataFetcher})
