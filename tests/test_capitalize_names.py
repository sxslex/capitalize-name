# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import capitalize_name


NAMES = {
    'BRASÍLIA': 'Brasília',
    'BRASÍLIA/PLANO PILOTO': 'Brasília/Plano Piloto',
    'joão paulo ii': 'João Paulo II',
    '': ''
}


def test_names():
    for name in NAMES:
        assert capitalize_name.capitalize(name) == NAMES[name]
