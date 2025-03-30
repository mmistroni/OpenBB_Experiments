import pytest

from openbb_providers.utils.damod_utils import get_roe

def test_roe():

    result = get_roe()
    assert result is not None
    print(type(result))


