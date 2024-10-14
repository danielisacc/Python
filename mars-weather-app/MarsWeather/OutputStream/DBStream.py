"""This Module is designed to accept data from the APIHandler class, then stream that output to a DB Connection"""

from ..APIHandler import APIHandler

class DBStream():
    def __init__(self, data: APIHandler) -> None:
        self.__data = APIHandler()