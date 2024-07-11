import pytest

from openbb_providers.utils.finviz_helpers import run_screener

@pytest.mark.record_http
def test_sample_screener():
    generic_filter = {'Market Cap.' : '+Small (over $300mln)',
                      'Average Volume' : 'Over 200K',
                      'Price' : 'Over $10',
                      'EPS growththis year' : 'Over 20%'
                      }

    data = run_screener(generic_filter)
    assert bool(data)


@pytest.mark.record_http
def test_get_sample_screener_with_exception():
    generic_filter_dict = {'Market Cap.' : 'all (over $300mln)',
                           'Average Volume' :'Over 200K'
                           }
    with pytest.raises(Exception) as exc_info:
        data = run_screener(generic_filter_dict)
    # these asserts are identical; you can use either one
    assert 'Invalid filter' in exc_info.value.args[0]



