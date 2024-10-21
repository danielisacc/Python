from .DBConnection import DBConnection
import sqlite3 as sql
from os import path
from datetime import datetime

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
            query=  """
                INSERT OR IGNORE INTO sols (sol, date_retrieved, season, first_utc, last_utc)
                VALUES(?,?,?,?,?);
            """
            params = (int(sol), datetime.now().date(), data[sol]['Season'], data[sol]['First_UTC'], data[sol]['Last_UTC'])
            self.__c.execute(query, params)

            query=  """
                INSERT OR IGNORE INTO AT (sol, av, ct, mn, mx)
                VALUES(?,?,?,?,?);
            """
            params = (int(sol), data[sol]['AT']['av'], data[sol]['AT']['ct'], data[sol]['AT']['mn'], data[sol]['AT']['mx'])
            self.__c.execute(query, params)

            query=  """
                INSERT OR IGNORE INTO HWS (sol, av, ct, mn, mx)
                VALUES(?,?,?,?,?);
            """
            params = (int(sol), data[sol]['HWS']['av'], data[sol]['HWS']['ct'], data[sol]['HWS']['mn'], data[sol]['HWS']['mx'])
            self.__c.execute(query, params)

            query=  """
                INSERT OR IGNORE INTO PRE (sol, av, ct, mn, mx)
                VALUES(?,?,?,?,?);
            """
            params = (int(sol), data[sol]['PRE']['av'], data[sol]['PRE']['ct'], data[sol]['PRE']['mn'], data[sol]['PRE']['mx'])
            self.__c.execute(query, params)

            query = """
                INSERT OR IGNORE INTO compass_pt
                (compass_pt_num, sol, compass_degrees,
                compass_point, compass_right, compass_up, ct)
                VALUES(?,?,?,?,?,?,?);
            """
            wd = data[sol]['WD']
            # cpn is the compass_point_num from the api documentation
            for cpn in wd:
                if cpn != 'most_common':
                    params = (int(cpn), int(sol), wd[cpn]['compass_degrees'], wd[cpn]['compass_point'], wd[cpn]['compass_right'], wd[cpn]['compass_up'], wd[cpn]['ct'])
                    self.__c.execute(query, params)


    def createDB(self):
        try:
            script_dir = path.dirname(__file__)
            sql_filepath = path.join(script_dir, "WeatherDataCreate.sql")
            with open(sql_filepath) as file:
                script = file.read()

            self.__c.executescript(script)
            self.__conn.commit()
        except FileNotFoundError:
            print("Error: WeatherDataCreate.sql Not Found.")
        except Exception as e:
            print(f"An error occurred: {e}")