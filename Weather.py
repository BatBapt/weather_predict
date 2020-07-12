import requests
import json
import configparser


class Weather:

    def __init__(self, location):
        self.location = location

        self.api_key = self.get_api_key()
        self.get_weather(self.api_key, location)

    def get_api_key(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['openweathermap']['api']

    def get_weather(self, key, location):
        """
        This function call the API, take the information about the weather in the city,
        write it in a file (same name of the city) and return a JSON document
        :param api_key: API key for the call
        :param location: City
        :return: return informations in JSON about the city
        """
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&metric".format(location, key)

        response = requests.get(url).json()
        filename = location + ".txt"
        with open(filename, 'w') as file:
            json.dump(response, file, indent=4)

    def extract_component(self, json_file):
        """

        :param json_file: JSON file to load the informations
        :return: Not implemented yet
        """
        with open(json_file) as file:
            data = json.load(file)

        temp = data["main"]["temp"] - 273
        print("Il fait actuellement {} °C".format(temp))