#!/usr/bin/env python3

import requests

# Public APIs can are available in  https://github.com/public-apis/public-apis#weather
# MetaWeather provides an API that delivers JSON over HTTPS for access to their data.
API_ROOT = 'https://www.metaweather.com'

# Location search URL. Argument should be a string.
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/' # + WOEID
