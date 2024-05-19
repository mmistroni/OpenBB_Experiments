"""Pyth Provider Module."""


from openbb_core.provider.abstract.provider import Provider
from openbb_fmp import fmp_provider
from openbb_providers.models.cftc import CommitmentOfTradersAnalysisFetcher
from openbb_providers.models.cftc_contracts import  CommitmentOfTradersReportFetcher
from openbb_providers.models.fmp_marketcap import FMPMarketCapDataFetcher
from openbb_providers.models.seekingalpha import SADividendPicksFetcher, SAStockIdeaFetcher


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




fmp_provider.fetcher_dict.update({
        "CommitmentOfTradersAnalysis": CommitmentOfTradersAnalysisFetcher,
        "CommitmentOfTradersReport": CommitmentOfTradersReportFetcher,
        "FMPMarketCapDataFetcher" : FMPMarketCapDataFetcher})
