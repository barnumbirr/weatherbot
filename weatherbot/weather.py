#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of weatherbot - A Twitter weather bot
# Copyright © 2014-2020 Martin Simon
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

import json
import requests
from . import (config, exception)

class Weather(object):

    _session = None
    __DEFAULT_BASE_URL = 'https://api.weatherapi.com/v1/forecast.json?key={0}&q={1},{2}&days=1&lang=en'
    __DEFAULT_TIMEOUT = 60

    def __init__(self, base_url = __DEFAULT_BASE_URL, request_timeout = __DEFAULT_TIMEOUT):
        self.base_url = base_url
        self.config = config.load()
        self.request_timeout = request_timeout

    @staticmethod
    def _create_session():
        session = requests.Session()
        user_agent = 'weatherbot - A  Twitter weather bot written \
                      in Python. (https://github.com/barnumbirr/weatherbot)'
        session.headers.update({'Content-Type': 'application/json'})
        session.headers.update({'User-agent': user_agent})
        return session

    def __request(self):
        response_object = self.session.get(self.base_url.format(self.config.get("weatherapi", "api_key"),
                                                                self.config.get("weatherapi", "latitude"),
                                                                self.config.get("weatherapi", "longitude")
                                                                ), timeout = self.request_timeout)

        try:
            response = json.loads(response_object.text)
        except Exception as e:
            raise exception.WeatherProviderError("{}".format(e))
        return response

    def data(self):
        response = self.__request()
        return response
