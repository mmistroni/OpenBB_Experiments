from openbb_terminal.sdk import openbb
import yfinance
import numpy as np

def best_fit_slope(y: np.array) -> float:
    '''
    Determine the slope for the linear regression line

    Parameters
    ----------
    y : TYPE
        The time-series to find the linear regression line for

    Returns
    -------
    m : float
        The gradient (slope) of the linear regression line
    '''

    x = np.arange(0, y.shape[0])

    x_bar = np.mean(x)
    y_bar = np.mean(y)

    return np.sum((x - x_bar) * (y - y_bar)) / np.sum((x - x_bar) ** 2)


def generate_trend_template(df):
    df['200_ma'] = df['Close'].rolling(200).mean()
    df['52_week_high'] = df['Close'].rolling(52 * 5).max()
    df['52_week_low'] = df['Close'].rolling(52 * 5).min()
    df['150_ma'] = df['Close'].rolling(150).mean()
    df['50_ma'] = df['Close'].rolling(50).mean()
    df['slope'] = df['200_ma'].rolling(40).apply(best_fit_slope)
    df['pricegt50avg'] = df['Close'] > df['50_ma']
    df['price30pctgt52wklow'] = (df['Close'] / df['52_week_low']) > 1.3
    df['priceWithin25pc52wkhigh'] = (df['Close'] / df['52_week_high']) > 0.8
    df['trend_template'] = (
            (df['Close'] > df['200_ma'])
            & (df['Close'] > df['150_ma'])
            & (df['150_ma'] > df['200_ma'])
            & (df['slope'] > 0)
            & (df['50_ma'] > df['150_ma'])
            & (df['50_ma'] > df['200_ma'])
            & (df['pricegt50avg'] == True)
            & (df['priceWithin25pc52wkhigh'] == True)
            & (df['priceWithin25pc52wkhigh'] == True)
    )

    return df

def get_historical_data(ticker):
    stock = yfinance.Ticker(ticker)
    return stock.history(period="20y")


def run():

    hist = get_historical_data('TX')



    templated = generate_trend_template(hist)

    ma_filter = (templated['trend_template'] == True)


    print(templated[ma_filter])



if __name__ == '__main__':
    run()



