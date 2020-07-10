import requests
import json
import configparser


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather(api_key, location):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&metric".format(location, api_key)

    response = requests.get(url).json()
    filename = location + ".txt"
    with open(filename, 'w') as file:
        json.dump(response, file, indent=4)


get_weather(get_api_key(), "Toulon")