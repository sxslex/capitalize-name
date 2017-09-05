# -*- coding: utf-8 -*-

import click
import capitalize_name


@click.command(help='capitalize_name `name`')
@click.argument('name')
def capitalize(name):
    print(capitalize_name.capitalize(name))


if __name__ == '__main__':
    capitalize()
