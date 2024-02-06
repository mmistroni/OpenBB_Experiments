import os

from mm_obb_extensions.utils.helpers import get_fmp_marketcap
def test_get_fmp_marketcap(monkeypatch):

    def get_key():
        return os.environ['FMPREPKEY']

    monkeypatch.setattr('mm_obb_extensions.utils.helpers.get_fmp_key', get_key)

    data = get_fmp_marketcap('AAPL')
    assert data is not None