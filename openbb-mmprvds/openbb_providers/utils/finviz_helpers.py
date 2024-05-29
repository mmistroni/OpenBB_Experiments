from finvizfinance.screener.overview import Overview

def run_screener(filters):
    foverview = Overview()
    foverview.set_filter(filters_dict=filters)
    df = foverview.screener_view()
    return df.to_dict('records') if df is not None else []
