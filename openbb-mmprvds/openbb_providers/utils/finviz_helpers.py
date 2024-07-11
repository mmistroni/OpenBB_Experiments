from finvizfinance.screener.overview import Overview
from typing import Any, Dict, List, Optional
def run_screener(filters:Dict[str, str]):
    foverview = Overview()

    foverview.set_filter(filters_dict=filters)
    df = foverview.screener_view()
    return df.to_dict('records') if df is not None else []


