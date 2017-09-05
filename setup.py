from setuptools import setup

setup(
    name='capitalize-name',
    version='1.0',
    url='https://github.com/sxslex/capitalize-name',
    download_url=(
        'https://github.com/sxslex/capitalize-name/archive/v1.0.tar.gz'
    ),
    author='SleX',
    author_email='sx.slex@gmail.com',
    description='Returns the correct writing of a compound name, respecting the first letters of the names in upper case.',
    keywords=['capitalize', 'name', 'compound name', 'upper'],
    packages=['capitalize_name'],
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
            'capitalizename = capitalize_name.cli:capitalize',
        ],
    },
)
