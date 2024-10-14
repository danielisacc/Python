from .DBConnection import DBConnection
import sqlite3 as sql
from os import path

class SQLiteConnection(DBConnection):
        
    def connect(self):
        self.__conn = sql.connect('WeatherData.db')
        self.__c = self.__conn.cursor()
        return 200
    
    def execute(self, query:str):
        self.__c.execute(query)
        return self.__c.fetchall()
    
    def disconnect(self):
        self.__conn.commit()
        self.__conn.close()

    def insert(self, data:dict):
        for sol in data['sol_keys']:
            sols_table =  """
                INSERT INTO sols (sol, date_retrieved, season, first_utc, last_utc)
                VALUES(?,?,?,?,?);
            """
            self.__c.execute(sols_table, ())

    def createDB(self):
        try:
            script_dir = path.dirname(__file__)
            sql_filepath = path.join(script_dir, "WeatherDataCreate.sql")
            with open(sql_filepath) as file:
                script = file.read()

            self.__c.executescript(script)
            self.__conn.commit()
        except FileNotFoundError:
            print("Error: File Not Found.")
        except Exception as e:
            print(f"An error occurred: {e}")