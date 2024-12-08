import pytest
from openbb_providers.utils import hor_fetcher
import re
import requests
from bs4 import BeautifulSoup
import asyncio

@pytest.mark.asyncio
async def test_fetch_data():
    test_year = '2020'
    result = await hor_fetcher.fetch_data(test_year)
    assert result is not None
    assert len(result) > 10
