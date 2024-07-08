from finvizfinance.screener.overview import Overview
from typing import Any, Dict, List, Optional
def run_screener(filters:List[str]):
    foverview = Overview()

    filters_unpacked = _unpack_filters(filters)

    foverview.set_filter(filters_dict=filters_unpacked)
    df = foverview.screener_view()
    return df.to_dict('records') if df is not None else []


def _unpack_filters(filters:List[str]) -> Dict[str,str]:
    # assuming a list of  filtername=filterval
    if filters:
        remapped = map(lambda filter_str: filter_str.split('='), filters)
        return dict((key, val) for key, val in remapped)
    return {}
