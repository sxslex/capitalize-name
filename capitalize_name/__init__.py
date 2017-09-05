# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import string
import sys
import re


__version__ = '1.0'


roman_pattern = re.compile(
    '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',
    re.VERBOSE
)


_ARTICLES = [
    'and', 'or', 'on', 'of', 'the',
    'a', 'o', 'em', 'e', 'da', 'de', 'di', 'do', 'du', 'das', 'dos', 'dus'
]

_SEPARATOR_CHARACTERS = string.whitespace + '/'

_IGNORE_WORLS = {}


def capitalize(
    full_name,
    articles=None,
    separator_characters=None,
    ignore_worls=None,
):
    """Returns the correct writing of a compound name, respecting the
    first letters of the names in upper case."""
    if articles is None:
        articles = _ARTICLES
    if separator_characters is None:
        separator_characters = _SEPARATOR_CHARACTERS
    if ignore_worls is None:
        ignore_worls = _IGNORE_WORLS
    new_full_name = full_name
    if hasattr(new_full_name, 'strip'):
        new_full_name = new_full_name.strip()
    if not new_full_name:
        return full_name
    new_full_name = deep_unicode(new_full_name)
    list_full_name = []
    start_idx = 0
    for step_idx, char in enumerate(list(new_full_name)):
        if char in separator_characters:
            list_full_name.extend(
                [
                    _setting_word(
                        new_full_name[start_idx:step_idx],
                        separator_characters, ignore_worls,
                        articles if list_full_name else []
                    ),
                    char
                ]
            )
            start_idx = step_idx + 1
    list_full_name.append(
        _setting_word(
            new_full_name[start_idx:],
            separator_characters, ignore_worls, articles
        )
    )
    return ''.join(list_full_name)


def _setting_word(word, separator_characters, ignore_worls, articles):
    if word in separator_characters:
        return word
    if word.lower() in ignore_worls:
        return ignore_worls[word.lower()]
    word = word.lower()
    if word in articles:
        return word
    word = word.upper()
    if roman_pattern.search(word):
        return word
    return word.capitalize()


def deep_unicode(s, encodings=None):
    """decode "DEEP" S using the codec registered for encoding."""
    if encodings is None:
        encodings = ['utf-8', 'latin-1']
    if isinstance(s, (list, tuple)):
        return [deep_unicode(i) for i in s]
    if isinstance(s, dict):
        return dict([
            (deep_unicode(key), deep_unicode(s[key]))
            for key in s
        ])
        # in_dict = {}
        # for key in s:
        #     in_dict[to_unicode(key)] = to_unicode(s[key])
        # return in_dict
    elif isinstance(s, str):
        for encoding in encodings:
            try:
                return s.decode(encoding)
            except:
                pass
    return s


def deep_encode(s, encoding='utf-8', errors='strict'):
    """Encode "DEEP" S using the codec registered for encoding."""
    # encoding defaults to the default encoding. errors may be given to set
    # a different error handling scheme. Default is 'strict' meaning
    # that encoding errors raise
    # a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
    # 'xmlcharrefreplace' as well as any other name registered with
    # codecs.register_error that can handle UnicodeEncodeErrors.
    s = deep_encode(s)
    if sys.version_info.major < 3 and isinstance(s, unicode):
        return s.encode(encoding, errors)
    if isinstance(s, (list, tuple)):
        return [deep_encode(i, encoding=encoding, errors=errors) for i in s]
    if isinstance(s, dict):
        return dict([
            (
                deep_encode(key, encoding=encoding, errors=errors),
                deep_encode(s[key], encoding=encoding, errors=errors)
            ) for key in s
        ])
        # new_dict = {}
        # for key in s:
        #     new_dict[
        #         to_encode(key, encoding=encoding, errors=errors)
        #     ] = to_encode(s[key], encoding=encoding, errors=errors)
        # return new_dict
    return s
