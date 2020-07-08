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

def forecast_printout(weather):
    print(f"The weather for {weather['title']}:")
    for entries in weather['consolidated_weather']:
        date = entries['applicable_date']
        high = entries['max_temp']
        low = entries['min_temp']
        state = entries['weather_state_name']
        print(f"On {date},it will have {state}, with highs of {high}°C and"
              f"lows of {low}°C.")

def get_forecast():
    try:
        which_place = input('Which place would you like to know the weather of? \n')
        this_place = location(which_place)
        woeid = this_place[0]['woeid']
        forecast_printout(weather(woeid))
    except requests.exceptions.ConnectionError:
        print("Please check your connection status. Cannot connect to server.")

if __name__ == '__main__':
    while True:
        get_forecast()
