import re


def get_substr(string, delim1, delim2, strip=True):
    """
    Return the a substring of a string between delimiters delim1 and delim2.
    If either delimiter isn't given, return substring from start or until the
    end of string. If multiple instances of delimiters are found, the outmost
    ones are used. If "strip" is set true, strip the result. If nothing is
    found, return None.
    :param string: String from which we search for substr (string)
    :param delim1: First delimiter (string)
    :param delim2: Second delimiter (string)
    :param strip: Toggle result stripping (boolean)
    :return: String or None
    """
    if not string or string == '':
        return None

    de1 = delim1 if delim1 else ''
    de2 = delim2 if delim2 else ''
    res = re.search(de1 + '(.*)' + de2, string)

    if not res:
        return None

    ret = str(res.group(1))

    if strip:
        ret = ret.strip()

    return ret


def get_nested_val(data, nested_key):
    """
    Return value of dictionary by nested key separated by a '.' character used
    in e.g. Mongodb notation.
    :param data: Nested dictionary
    :param nested_key: Nested key (Example "level1.level2.level3")
    :return: Value of field or None if the field doesn't exist, true or false
    regarding whether value was found or not in case actual value can be None
    (boolean).
    """
    if not data or not nested_key or nested_key == '':
        return None, False

    ds = nested_key.split('.')
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
