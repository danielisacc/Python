""" Module designed to handle API requests, data parsing,
and sending data to sources such as DataModeling Objects and OutputStreams."""
import requests as rq
from os import getenv
class APIError(Exception):
    pass

class APIKeyError(APIError):
    pass

class FailedAPIConnection(APIError):
    pass

class APIHandler():
    def __init__(self) -> None:
        self.__apiParams = {
            "url": "https://api.nasa.gov/insight_weather/",
            "api_key": getenv("MARS_WEATHER_API_KEY"),
            "feedType": "json",
            "ver": "1.0"
        }
        self.__response = None
    
    def connect(self) -> str:
        if self.__apiParams['api_key'] == None:
            self.__apiParams['api_key'] = input("API Key not provided in MARS_WEATHER_API_KEY enviornemntal variable. Please enter an API key now for temporary acces, or check documentation for information on setting up enviornmental variable.\nPlease enter an temporary API Key: ").strip()
        getString = f"{self.__apiParams['url']}?api_key={self.__apiParams['api_key']}&feedtype={self.__apiParams['feedType']}&ver={self.__apiParams['ver']}"
        response = rq.get(getString)
        if response.status_code == 403:
            raise APIKeyError(f"Incorrect API Key: 401 Status Code, Forbidden User Access: input get request\n{getString}")
        self.__response = response
        return self.__response.status_code


    def getJSON(self):
        if self.__response == None:
            raise FailedAPIConnection("No Connection Created: Please run APIHandler.Obj.connect()")
        if self.__response.status_code != 200:
            raise FailedAPIConnection("Connection to API was unsuccessful")
        return self.__response.json()