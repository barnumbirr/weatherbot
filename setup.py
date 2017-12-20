#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of weatherbot - A Twitter weather bot
# Copyright © 2014-2017 Martin Simon
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

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'weatherbot',
    version = '0.1',
    url = 'https://github.com/mrsmn/weatherbot',
    download_url = 'https://github.com/mrsmn/weatherbot/archive/master.zip',
    author = 'Martin Simon <me@martinsimon.me>',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['weatherbot'],
    description = 'weatherbot is an APACHE licensed Twitter weather bot written in Python.',
    long_description = open('README.md','r').read(),
    install_requires=['tweepy'],
    keywords = ['weather forecast', 'forecast', 'tweepy', 'twitter'],
)
