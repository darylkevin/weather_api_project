#!/usr/bin/env python3

import requests

# Public APIs can are available in:
# https://github.com/public-apis/public-apis#weather
# MetaWeather provides an API that delivers JSON over HTTPS for
# access to their data.
API_URL = 'https://www.metaweather.com'

# Location search URL. Argument should be a string. This provides a WOEID which
# we will use later to get the weather.
API_LOCATION = '/api/location/search/?query='

# After taking the WOEID from the location query, we will use that to get the
# actual weather for that location.
API_WEATHER = '/api/location/'  # + WOEID

# Block where program will send requests to the web API.


def location(input):
    return requests.get(API_URL + API_LOCATION + input).json()


def weather(woeid):
    return requests.get(API_URL + API_WEATHER + str(woeid)).json()


# Block of code which I intergrated from my Udacity course.
# This helps eliminate ambiguity in user input.
def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['title']}")


# This is the terminal output which prints out the weather for the user to see.
def forecast_printout(weather):
    print(f"The weather for {weather['title']}:")
    for entries in weather['consolidated_weather']:
        date = entries['applicable_date']
        high = entries['max_temp']
        low = entries['min_temp']
        state = entries['weather_state_name']
        print(f"On {date},it will have {state}, with highs of {high}°C and"
              f"lows of {low}°C.")


# Program asks user for which place they would like to know the weather of.
def get_forecast():
    try:
        # I integrated this block of code from my Udacity
        # Python course which improves error handling in the
        # weather program. This elimiates ambiguity in user input.
        which_place = ''
        while not which_place:
            which_place = input('Which place would you like to '
                                'know the weather of? \n')
        this_place = location(which_place)
        if len(this_place) == 0:
            print('I don\'t think that\'s a real location.')
        elif len(this_place) > 1:
            disambiguate_locations(this_place)
        else:
            woeid = this_place[0]['woeid']
            forecast_printout(weather(woeid))
    except requests.exceptions.ConnectionError:
        print("Please check your connection status. Cannot connect to server.")


if __name__ == '__main__':
    while True:
        get_forecast()
