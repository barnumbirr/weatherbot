<h1><img src="https://raw.github.com/barnumbirr/weatherbot/master/images/weatherbot.png" height=55 alt="weatherbot" title="weatherbot"> weatherbot</h1>

**weatherbot** is an APACHE licensed [Twitter](https://twitter.com) weather bot written in Python. It is designed to tweet weather conditions and forecasts from [WeatherAPI.com](https://www.weatherapi.com/).
An instance of this bot [currently lives here](https://twitter.com/luxweather). This library has been tested with Python 3.6+ only.

## Installation:

From source use

```bash
$ git clone https://github.com/barnumbirr/weatherbot.git /etc/weatherbot
```

Edit the config.sample file to suit your needs and create a cron job like this:

```bash
$ 30 * * * * python /etc/weatherbot/bin/weatherbot
```

## License:

```
Copyright 2014-2021 Martin Simon

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

```

## Acknowledgement:

This project's structure is heavily inspired by [Radicale - A simple CalDAV (calendar) and CardDAV (contact) server](https://github.com/Kozea/Radicale).

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
BTC : bc1qq04jnuqqavpccfptmddqjkg7cuspy3new4sxq9
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
ETH : 0x2238A11856428b72E80D70Be8666729497059d95
LTC : MQwXsBrArLRHQzwQZAjJPNrxGS1uNDDKX6
```
