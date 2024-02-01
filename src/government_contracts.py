from openbb import obb
import logging

def run():
    TICKER = 'DIS'
    obb.account.login(email='mmistroni@gmail.com', password='M15tr0n1;')
    obb.user.preferences.output_type = "dataframe"

    df = obb.equity.fundamental.overview(symbol=TICKER)
    print(df)


if __name__ == '__main__':
    run()
