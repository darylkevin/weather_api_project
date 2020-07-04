#!/usr/bin/env python3

import requests

# Public APIs can are available in  https://github.com/public-apis/public-apis#weather
# MetaWeather provides an API that delivers JSON over HTTPS for access to their data.
API_URL = 'https://www.metaweather.com'

# Location search URL. Argument should be a string. This provides a WOEID which
# we will use later to get the weather.
API_LOCATION = '/api/location/search/?query='

# After taking the WOEID from the location query, we will use that to get the
# actual weather for that location.
API_WEATHER = '/api/location/' # + WOEID

def location(input):
    return requests.get(API_URL + API_LOCATION + input).json()

def weather(woeid):
    return requests.get(API_URL + API_WEATHER + str(woeid)).json()


