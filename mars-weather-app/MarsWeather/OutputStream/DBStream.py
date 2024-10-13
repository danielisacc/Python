"""This Module is designed to accept data from the APIHandler class, then stream that output to a DB Connection"""

from APIHandler import APIHandler
from abc import ABC, abstractmethod

import sqlite3
class DBStream():
    def __init__(self, data: APIHandler) -> None:
        self.__data = APIHandler()
    
class DBConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, data:APIHandler):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class SQLiteConnection(DBConnection):
        
    def connect(self):
        self.__conn = sqlite3.connect('WeatherData.db')
        self.__c = self.__conn.cursor()
    
    def execute(self, data: APIHandler):
        self.__c.execute()
    
    def disconnect(self):
        return super().disconnect()

    def createDB(self):
        self.__c.execute("""""")


class MySQLConnection(DBConnection):
    def connect(self):
        return super().connect()
    
    def execute(self, data: APIHandler):
        return super().execute(data)
    
    def disconnect(self):
        return super().disconnect()