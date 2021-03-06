#!/usr/bin/env python
"""Setuptools script.
"""
import os
import codecs
from setuptools import setup, find_packages

PACKAGENAME = 'lsst-dochub-proto'
DESCRIPTION = 'Prototype of LSST DocHub as a static website generator'
AUTHOR = 'Adam Thornton'
AUTHOR_EMAIL = 'athornton@lsst.org'
URL = 'https://github.com/sqre-lsst/dochub-prototype'
VERSION = '0.0.3'
LICENSE = 'MIT'


def local_read(filename):
    """Convenience function for includes"""
    full_filename = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        filename)
    return codecs.open(full_filename, 'r', 'utf-8').read()


LONG_DESC = local_read('README.rst')

setup(
    name=PACKAGENAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESC,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='lsst',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=[
        'requests>=2.13.0,<3.0.0',
        'pyyaml>=3.12,<4.0.0',
        'Jinja2>=2.9,<3.0.0',
        'sqre-apikit>=0.1.1,<1.0.0',
        'ltd-conveyor>=0.3.1,<0.4.0'
    ],
    entry_points={
        'console_scripts': [
            'dochub-prototype = dochubproto.cli:main'
        ]
    }
)
