import datetime as dt
import requests


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "cae48463a0ae3ff4302fd966fc23b052"
CITY = "London"


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit
    

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()


temp_Kelvin = response["main"]["temp"]
temp_Celsius, temp_Fahrenheit = kelvin_to_celsius(temp_Kelvin)
feels_like_kelvin = response["main"]["feels_like"]
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius(feels_like_kelvin)
wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_utc = dt.datetime.utcfromtimestamp(response["sys"]["sunrise"])
sunset_utc = dt.datetime.utcfromtimestamp(response["sys"]["sunset"])


print (f"Tepreature in {CITY}: {temp_Celsius:.2f}°C / {temp_Fahrenheit:.2f}°F")
print (f"Tepreature in {CITY}:feels like {feels_like_celsius:.2f}°C or {feels_like_fahrenheit}")
print (f"Humidity in {CITY}: {humidity}%")
print (f"Wind speed in {CITY}: {wind_speed}km/h")
print (f"General weather in {CITY}: {description}")
print (f"sunrises in {CITY} at {sunrise_utc} local time.")
print (f"sunsets in {CITY} at {sunset_utc} local time.")



