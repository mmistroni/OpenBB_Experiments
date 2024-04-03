import pytest

"""Pyth2 Fetchers tests."""
import pytest
from openbb_mmext.utils.helpers import get_nymo, get_nysi
import re
import requests
from bs4 import BeautifulSoup

#
@pytest.mark.vcr()
def test_get_nymo():

    res_dict = get_nymo()
    assert res_dict is not None
    nymo = res_dict['VALUE']
    assert nymo == -28.14

@pytest.mark.vcr()
def test_get_nysi():

    res_dict = get_nysi()
    assert res_dict is not None
    assert res_dict['VALUE'] == 855.75









