import pytest

from openbb_providers.utils.damod_utils import get_roe, get_ps, get_fgrowtheps, get_pvdata,\
                                        get_pe, get_institutional_holders, get_betas

def test_roe():

    result = get_roe()
    assert result is not None
    print(type(result))

def test_get_ps():
    '''
    Revenue Multiples by Sector (US)
    https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/psdata.html
    '''
    result = get_ps()
    assert result is not None

def test_get_fgrowtheps():
    result = get_fgrowtheps()
    assert result is not None

def test_get_pe():
    result = get_pe()
    assert result is not None
'Current PE', 'Trailing PE', 'Forward PE', 'Expected Growth - next 5 years', 'PEG Ratio'

def test_get_instholders():
    result = get_institutional_holders()
    assert result is not None

def test_get_pvdata():
    result = get_pvdata()
    assert result is not None

def test_get_betas():
    result = get_betas()
    assert result is not None
