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

Cloned GitHub repo
How did you "install" OpenBB after this?
It works.
cd.. into your extension directory, and install pip install -e .
Then, from openbb import obb fails?



(openbb_latest) C:\Users\Marco And Sofia\OpenBB\OpenBB_Experiments\pyth2>python
Python 3.11.8 | packaged by Anaconda, Inc. | (main, Feb 26 2024, 21:34:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from openbb import obb
Extensions to add: pyth2@1.0.0

Building...



(openbb_latest) C:\Users\Marco And Sofia\OpenBB\OpenBB_Experiments\pyth2>python
Python 3.11.8 | packaged by Anaconda, Inc. | (main, Feb 26 2024, 21:34:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from openbb import obb
Extensions to add: pyth2@1.0.0

Building...

To launch the API you can run: uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 8000 --reload
You can specify the host and port parameters on that command - this might also help: