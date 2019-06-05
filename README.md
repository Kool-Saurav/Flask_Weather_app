# Flask Wearther app ☀️☔️

This is a Flask (Python) application that auto-detects local weather based off of user's external IP address and weather of the city user enters.

<img src="https://github.com/Kool-Saurav/Flask_Weather_app/blob/master/static/images/weather_example.png">
_Example screenshot of Flask Wearther app application_

## Setup

- Install dependencies from pipflie that is located in project directory
  - Open command prompt in that directory and run below commands  
  - `pip install pipenv`
  - `pipenv install requests`
  - `pipenv install flask`
 
- Activate virtualenv using command **pipenv shell**
- Run this command in cmd
  - `pipenv run python -m flask run`


## Functionality

Gets a user's external IP address using this link (https://ipapi.co/city/). To get more specific location information to pass into Weather API (https://www.apixu.com/). Weather information (current temperature and % chance of rain) is returned based on the location associated with the IP and name of city.

To work on this locally clone the repo, request and add an API key (locally) from Apixu and then run `app.py`

`index_1.html` displays the weather information and displays appropriate weather icon (https://cdn.apixu.com/weather/64x64/day/weather_icon.png) based on what the current weather is.

To display temperature in Celsius instead of Fahrenheit.

## Sample Output:

### Today's Weather Forecast for Ludhiana, Punjab

Right now it is 39.6°C and Party cloudy.

### Today's Weather Forecast for City, State

Right now it is X° and there is a Y% chance of rain.
