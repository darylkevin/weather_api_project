# Weather API Project 

This project is from my Udacity course on Python and using Web APIs. I am committing my excercises in this repository and adding changes to the code which was corrected during the course. Most of the code will resemble what was walked through in that assignment.

## What is this project for?

This project aims to showcase how I am able to retrieve data from a weather website API. A list of public APIs can be found in `https://github.com/public-apis/public-apis`. 

I am using MetaWeather webiste as the source of the weather predictions.

## What does this project do?

This program takes information about the weather from MetaWeather website and displays it in the terminal.

The program asks the user to input a city name where they would like to know the weather. The program takes the input and queries the website about the place's WOEID (Where On Earth ID). 

Once the WOEID is obtained, the program then takes the WOEID and queries the website about the weather on that place. The output obtained is in JSON format. From the data available in the JSON output, the program then extracts the information to be displayed and parses that information in human readable format.

## What technologies does this project use?

This project is built mainly using Python. A basic understanding of public web APIs were also beneficial in developing this project.

## How can I use this?
 

## Road map for this project

The project is only giving output only on the terminal. I plan to make a frontend interface where a user without knowledge of the terminal can still use the program easily.
