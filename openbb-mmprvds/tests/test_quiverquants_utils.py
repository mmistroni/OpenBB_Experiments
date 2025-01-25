import pytest

from openbb_providers.utils.quiverquants_utils import get_government_contracts

def test_get_government_contracts():
    res = get_government_contracts()
    assert res is not None
    assert res.shape[0] > 1
    