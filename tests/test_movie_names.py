# -*- coding: utf-8 -*-

import capitalize_name


MOVIES = {
    'THE usual suspects': 'The Usual Suspects',
    'home ALONE': 'Home Alone',
    'the 400 blows': 'The 400 Blows',
    'ace ventura: pet detective': 'Ace Ventura: Pet Detective',
    'pirates of the caribbean': 'Pirates of the Caribbean',
    'gangs of New York ': 'Gangs of New York',
    'THE GODFATHER: PART II': 'The Godfather: Part II'
}


def test_movie_names():
    for movie in MOVIES:
        assert capitalize_name.capitalize(movie) == MOVIES[movie]
