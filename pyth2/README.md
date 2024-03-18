# OpenBB CIRO Provider

This extension integrates the [CIRO](https://www.ciro.ca/) data provider into the OpenBB Platform.

## Installation

To install the extension:

```bash
pip install openbb-ciro
```

For development please check [Contribution Guidelines](https://github.com/OpenBB-finance/OpenBBTerminal/blob/feature/openbb-sdk-v4/openbb_platform/CONTRIBUTING.md).

Documentation available [here](https://docs.openbb.co/sdk).

https://bvb.ro/TradingAndStatistics/Trading/MiFID_II_PostTradeListForDownload.ashx?filetype=xlsx


pyproject.toml we define the extension

```pyth2 = "openbb_pyth2:pyth2_provider"```

This provider is then defined in  openbb_pyth2\__init__.py

The provider would refer to a fetcher which is defined in openbb_pyth2.models.__init__.py

#### Steps to get there

1. Create an anaconda env
2. Use this env to get openbb from git    git clone https://github.com/OpenBB-finance/OpenBBTerminal.git
3. Build openbb following instructions here https://docs.openbb.co/platform/installation#source
4. Test the build 
        from openbb import obb
        obb.account.login(email='mmistroni@gmail.com', password='**')
        obb.user.preferences.output_type = "dataframe"
        obb.equity.price.historical(symbol = 'XOM', provider='fmp')
5. Build your extension
6. Run a simple unit test to verify you can import libraries from OBB

cd 





