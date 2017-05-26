
from setuptools import setup, find_packages

import geo_ip_service

setup(
    name='geo_ip_service',
    version='1.0',
    packages=find_packages(),
    long_description='long description',
    install_requires=['geoip2', 'aiohttp==2.0.7'],
    entry_points={
        'console_scripts': [
                'geo-ip-service = geo_ip_service.main',
            ]
    }
)

#  USAGE:
 #geo-ip-service --action start --dbpath  /root/data/maxmind/GeoLite2-City.mmdb
