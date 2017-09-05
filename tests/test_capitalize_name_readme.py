# -*- coding: utf-8 -*-

import capitalize_name


def test_capitalize_name_readme():
    assert capitalize_name.capitalize(
        'AV. DOM PEDRO DE ALMEIDA I'
    ) == 'Av. Dom Pedro de Almeida I'
