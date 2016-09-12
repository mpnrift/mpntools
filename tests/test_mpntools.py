import pytest
import mpntools as mpn


############################
# Tests for get_substr()
############################


def test_get_substr_normal():
    ret = mpn.get_substr('start middle end', 'start', 'end', strip=True)
    assert ret is not None
    assert ret == 'middle'


def test_get_substr_no_strip():
    ret = mpn.get_substr('start middle end', 'start', 'end', strip=False)
    assert ret is not None
    assert ret == ' middle '


def test_get_substr_start():
    ret = mpn.get_substr('start middle end', None, 'end', strip=True)
    assert ret is not None
    assert ret == 'start middle'


def test_get_substr_end():
    ret = mpn.get_substr('start middle end', 'start', None, strip=True)
    assert ret is not None
    assert ret == 'middle end'


def test_get_substr_no_result():
    ret = mpn.get_substr(
        'start middle end', 'beginning', 'finish', strip=True)
    assert ret is None


def test_get_substr_no_string():
    with pytest.raises(ValueError):
        mpn.get_substr(None, 'start', 'end', strip=True)


def test_get_substr_empty_string():
    with pytest.raises(ValueError):
        mpn.get_substr('', 'start', 'end', strip=True)


def test_get_substr_not_bool():
    with pytest.raises(ValueError):
        mpn.get_substr('string', 'start', 'end', strip='xyz')


############################
# Tests for get_substr_all()
############################


def test_get_substr_all_normal():
    ret = mpn.get_substr_all(
        'st b en st a en st c en', 'st', 'en', strip=True, sort=False)
    assert ret == ['b', 'a', 'c']


def test_get_substr_all_no_result():
    ret = mpn.get_substr_all(
        'st b en st a en', 'xx', 'yy', strip=False, sort=False)
    assert ret is None


def test_get_substr_all_sort():
    ret = mpn.get_substr_all(
        'st b en st a en st c en', 'st', 'en', strip=True, sort=True)
    assert ret == ['a', 'b', 'c']


def test_get_substr_all_no_strip():
    ret = mpn.get_substr_all(
        'st b en st a en st c en', 'st', 'en', strip=False, sort=False)
    assert ret == [' b ', ' a ', ' c ']


def test_get_substr_all_no_string():
    with pytest.raises(ValueError):
        mpn.get_substr_all(
            None, 'st', 'en', strip=False, sort=False)


def test_get_substr_all_empty_string():
    with pytest.raises(ValueError):
        mpn.get_substr_all(
            '', 'st', 'en', strip=False, sort=False)


def test_get_substr_all_not_bool():
    with pytest.raises(ValueError):
        mpn.get_substr_all(
            'string', 'st', 'en', strip='xyz', sort=False)


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
    with pytest.raises(ValueError):
        mpn.get_nested_val({}, 'somekey')


def test_get_nested_val_no_dict():
    with pytest.raises(ValueError):
        mpn.get_nested_val(None, 'somekey')


def test_get_nested_val_empty_key():
    with pytest.raises(ValueError):
        mpn.get_nested_val({'level1': {'level2': 'val'}}, '')


def test_get_nested_val_no_key():
    with pytest.raises(ValueError):
        mpn.get_nested_val({'level1': {'level2': 'val'}}, None)


def test_get_nested_val_null_value():
    ret0, ret1 = mpn.get_nested_val(
        {'level1': {'level2': None}}, 'level1.level2')
    assert ret0 is None
    assert ret1 is True
