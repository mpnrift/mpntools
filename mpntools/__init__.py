import re


def get_substr(st, de1, de2, strip=True):
    """
    Return the first occurrence of a substring between delimiters delim1 and
    delim2 from a string. If either delimiter isn't given, return substring
    from start or until the end of string. If strip is set true, strip the
    result. If nothing is found, return None.
    :param st: String from which we search for substr
    :param de1: First delimiter (string)
    :param de2: Second delimiter (string)
    :param strip: Toggle result stripping (boolean)
    :return: String or None
    """
    if not st or st == '' or not isinstance(strip, bool):
        raise ValueError

    res = re.search(
        (de1 if de1 else '') + '(.*)' + (de2 if de2 else ''), st)

    if not res:
        return None

    ret = str(res.group(1))

    if strip:
        ret = ret.strip()

    return ret


def get_substr_all(st, de1, de2, strip=True, sort=False):
    """
    Return all occurrences of substring between delimiters delim1 and delim2
    from a string. If strip is set true, strip the result. If sort is true,
    sort results before returning. Returns None if nothing was found.
    :param st: String from which we search for substr
    :param de1: First delimiter (string)
    :param de2: Second delimiter (string)
    :param strip: Toggle result stripping (boolean)
    :param sort: Toggle result sorting (boolean)
    :return: List or None
    """
    if (not st or st == '' or not de1 or de1 == '' or not de2 or de2 == ''
            or not isinstance(strip, bool) or not isinstance(sort, bool)):
        raise ValueError

    ret = re.findall(de1 + '(.*?)' + de2, st, re.DOTALL)

    if not ret:
        return None

    if strip:
        ret = [r.strip() for r in ret]

    if sort:
        ret = sorted(ret)

    return ret


def get_nested_val(data, key):
    """
    Return value of dictionary by nested key separated by a '.' character used
    in e.g. Mongodb notation.
    :param data: Nested dictionary
    :param key: Nested key (Example "level1.level2.level3")
    :return: Value of field or None if the field doesn't exist, true or false
    regarding whether value was found or not (in case actual value can be None)
    (boolean).
    """
    if not data or not key or key == '':
        raise ValueError

    ds = key.split('.')
    d_tmp = dict(data)
    i = 0

    while i < len(ds):
        if i == len(ds) - 1:
            if ds[i] in d_tmp:
                return d_tmp[ds[i]], True

        else:
            if ds[i] in d_tmp:
                d_tmp = d_tmp[ds[i]]

            else:
                return None, False

        i += 1

    return None, False
