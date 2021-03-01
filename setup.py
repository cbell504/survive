#!usr/bin/env python3

from setuptools import setup

setup(
    name='survive',
    packages=['survive'],
    package_dir={'survive': 'survive'},
    version='1.0.0',
    description='A simple backup script',
    author='Azurras',
    url='https://github.com/Azurras/backedup.git',
    author_email='',
    keywords=['survive'],
    entry_points={'console_scripts': [
        'survive = survive.__main__:main',
    ], },
)