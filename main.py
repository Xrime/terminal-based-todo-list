

import json
import requests
import os
from dotenv import load_dotenv
import sys
load_dotenv()
import argparse

        
load_favorite_json= "favorite.json"

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

weather_parser = subparsers.add_parser("weather", help="check weather")
weather_parser.add_argument("city", type=str, help="Name of the city or country that you want to check")
weather_parser.add_argument("-t" ,"--temp", action="store_true" , help="Check city temp")
weather_parser.add_argument("-Hum" ,"--humidity", action="store_true" , help="Check city humidity")
weather_parser.add_argument("-f" ,"--favorite", action="store_true" , help="Save city weather to favorite")
args = parser.parse_args()


API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Missing API_KEY in environment")
    sys.exit(1)


if args.command=="weather":
    city = args.city
    request = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": API_KEY, "units": "metric"},
    )

    api_parsed = request.json()
    temperature = api_parsed['main']['temp']
    humidity = api_parsed['main']['humidity']
    country = api_parsed['sys']['country']
    description = api_parsed['weather'][0]['description']

    if args.temp:
        print(f"The {city} temperature is {temperature} and there is {description}")
    elif args.humidity:
        print(f"The humidity is currently {humidity} in {country} {city}")
    elif args.favorite:
        with open(load_favorite_json, "w") as file:
            json.dump(city, file, indent=2)

