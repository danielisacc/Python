from MarsWeather.OutputStream.DBConnections.SQLite3Connection import SQLiteConnection
from MarsWeather import APIHandler as api

api = api.APIHandler()

api.connect()

data = api.getJSON()

dbConnection = SQLiteConnection()

print(dbConnection.connect())

dbConnection.createDB()

dbConnection.insert(data)

print(dbConnection.execute('SELECT av FROM PRE'))

dbConnection.disconnect()
