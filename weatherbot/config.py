#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of weatherbot - A Twitter weather bot
# Copyright © 2014-2018 Martin Simon
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

import os
import ConfigParser
from . import exception

def load(path='/etc/weatherbot/config'):
    config = ConfigParser.SafeConfigParser(allow_no_value=False)

    if os.path.isfile(path) and os.access(path, os.R_OK):
        config.read(path)
    else:
        raise exception.ConfigFileNotFound("Please read instructions in config.sample file.")
    return config
