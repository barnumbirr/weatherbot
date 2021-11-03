#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of weatherbot - A Twitter weather bot
# Copyright © 2014-2021 Martin Simon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# To use a consistent encoding
from os import path
from codecs import open
# Always prefer setuptools over distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'weatherbot',
    packages = ['weatherbot'],
    version = '0.3.1',
    description = 'weatherbot is an APACHE licensed Twitter weather bot written in Python.',
    author = 'Martin Simon',
    author_email = 'me@martinsimon.me',
    url = 'https://github.com/barnumbirr/weatherbot',
    project_urls={
        'Bug Reports': 'https://github.com/barnumbirr/weatherbot/issues',
        'Buy me a coffee': 'https://github.com/barnumbirr/weatherbot#buy-me-a-coffee',
    },
    license = 'Apache v2.0 License',
    install_requires=[
    'requests>=2.18.4',
    'tweepy>=3.5.0'
    ],
    keywords = ['weather forecast', 'forecast', 'tweepy', 'twitter'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications',
    ],
    long_description = long_description,
    long_description_content_type='text/markdown',
)
