#!/usr/bin/env python
from __future__ import print_function
"""EM Examples

EM examples is a set up utility codes and jupyter notebooks
that accompany the web-resource http://em.geosci.xyz
"""

from distutils.core import setup
from setuptools import find_packages


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS',
    'Natural Language :: English',
]

with open('README.rst') as f:
    LONG_DESCRIPTION = ''.join(f.readlines())

setup(
    name = 'cheddar',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        'future',
        'datetime',
        'parse',
        'properties'
    ],
    author = 'Lindsey Heagy',
    author_email = 'lindseyheagy@gmail.com',
    description = 'cheddar',
    long_description = LONG_DESCRIPTION,
    keywords = 'photos, videos',
    download_url = 'https://github.com/lheagy/cheddar',
    classifiers=CLASSIFIERS,
    platforms = ['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix'],
    license='MIT License',
    use_2to3 = False,
)
