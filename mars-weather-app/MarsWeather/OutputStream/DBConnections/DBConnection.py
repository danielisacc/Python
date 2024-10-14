from abc import ABC, abstractmethod

class DBConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query:str):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def insert(self, data:dict):
        pass