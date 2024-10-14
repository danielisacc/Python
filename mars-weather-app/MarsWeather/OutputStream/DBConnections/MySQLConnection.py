from .DBConnection import DBConnection

class MySQLConnection(DBConnection):
    def connect(self):
        return super().connect()
    
    def execute(self, query:str):
        return super().execute(query)
    
    def disconnect(self):
        return super().disconnect()
    
    def insert(self, data:dict):
        pass