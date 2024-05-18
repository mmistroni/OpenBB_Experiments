"""Pyth Provider Module."""


from openbb_core.provider.abstract.provider import Provider
from openbb_fmp import fmp_provider
from openbb_providers.models.cftc import CommitmentOfTradersAnalysisFetcher
from openbb_providers.models.cftc_contracts import  CommitmentOfTradersReportFetcher


cftc_provider = Provider(
    name="cftc",
    website="https://pyth.network/",
    description=(
        "Provider for fetching CFTC data via FMP."
    ),
    fetcher_dict={}
)



fmp_provider.fetcher_dict.update({
        "CommitmentOfTradersAnalysis": CommitmentOfTradersAnalysisFetcher,
        "CommitmentOfTradersReport": CommitmentOfTradersReportFetcher})
