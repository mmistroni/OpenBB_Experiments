import pytest
import requests

@pytest.mark.record_http
def test_some_test(record):
    requests.get('http://www.google.com')

