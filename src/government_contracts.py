from openbb_terminal.sdk import openbb

def run():
    latest_contracts = openbb.stocks.gov.lastcontracts()
    print('here it is')
    print(latest_contracts.head())

if __name__ == '__main__':
    run()
