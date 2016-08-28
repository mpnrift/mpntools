import pytest
import mpntools as mpn


############################
# Tests for get_substr_mid()
############################


def test_get_substr_mid_normal():
    ret = mpn.get_substr_mid('start middle end', 'start', 'end', strip=True)
    assert ret is not None
    assert ret == 'middle'


def test_get_substr_mid_no_strip():
    ret = mpn.get_substr_mid('start middle end', 'start', 'end', strip=False)
    assert ret is not None
    assert ret == ' middle '


def test_get_substr_mid_start():
    ret = mpn.get_substr_mid('start middle end', None, 'end', strip=True)
    assert ret is not None
    assert ret == 'start middle'


def test_get_substr_mid_end():
    ret = mpn.get_substr_mid('start middle end', 'start', None, strip=True)
    assert ret is not None
    assert ret == 'middle end'


def test_get_substr_mid_no_result():
    ret = mpn.get_substr_mid(
        'start middle end', 'beginning', 'finish', strip=True)
    assert ret is None


def test_get_substr_mid_no_string():
    ret = mpn.get_substr_mid(None, 'start', 'end', strip=True)
    assert ret is None


def test_get_substr_mid_empty_string():
    ret = mpn.get_substr_mid('', 'start', 'end', strip=True)
    assert ret is None


############################
# Tests for get_nested_val()
############################


def test_get_nested_val_normal():
    ret0, ret1 = mpn.get_nested_val(
        {'level1': {'level2': {'level3': 'val'}}}, 'level1.level2.level3')
    assert ret0 == 'val'
    assert ret1 is True


def test_get_nested_val_no_level():
    ret0, ret1 = mpn.get_nested_val(
        {'level1': {'level2': 'val'}}, 'level1.level2.level3')
    assert ret0 is None
    assert ret1 is False


def test_get_nested_val_empty_dict():
    ret0, ret1 = mpn.get_nested_val({}, 'somekey')
    assert ret0 is None
    assert ret1 is False


def test_get_nested_val_no_dict():
    ret0, ret1 = mpn.get_nested_val(None, 'somekey')
    assert ret0 is None
    assert ret1 is False


def test_get_nested_val_empty_key():
    ret0, ret1 = mpn.get_nested_val({'level1': {'level2': 'val'}}, '')
    assert ret0 is None
    assert ret1 is False


def test_get_nested_val_no_key():
    ret0, ret1 = mpn.get_nested_val({'level1': {'level2': 'val'}}, None)
    assert ret0 is None
    assert ret1 is False


def test_get_nested_val_null_value():
    ret0, ret1 = mpn.get_nested_val(
        {'level1': {'level2': None}}, 'level1.level2')
    assert ret0 is None
    assert ret1 is True
