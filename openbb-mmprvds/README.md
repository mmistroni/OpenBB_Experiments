# OpenBB Custom Providers

This is an attempt to write some extensions for the OpenBB platform.

Extensions in this repo contains
- CFTC Commitment of Traders (via FMP)
  - Get all Commitment of traders contracts via route obb.mmcftc.cot_list
  - Get commitment of traders for particular contract via route obb.mmcftc.cot(symbol='VX')
- Seeking Alpha news
  - Dividend Picks article
  - Stock Ideas articles
- FMP MarketCap 
  - retrieves historical market cap from FMP
- Jim Cramer's recommendation
  - fetches Jim Cramer Stock Picks
- Finviz Canslim provider
  - Leverages Finviz screener API (unofficial) to retrieve stocks according to canslim criteria. IMHO Finviz has 
    a more flexible screener than FMP, but the API i am using is 'sort of' unofficial. 

# set result preferences as dataframe, for better display obb.user.preferences.output_type = "dataframe"
