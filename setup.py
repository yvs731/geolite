
from os.path import join, dirname

from setuptools import setup, find_packages

import geolite

setup(
    name='geolite',
    version='1.0',
    packages=find_packages(),
    long_description='long description',
    install_requires=['aiohttp==2.0.7'],
    entry_points={
        'console_scripts': [
                'serve = geolite.main',
            ]
    }
)
