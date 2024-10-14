from MarsWeather.OutputStream.DBConnections.SQLite3Connection import SQLiteConnection
from MarsWeather import APIHandler as api

dbConnection = SQLiteConnection()

print(dbConnection.connect())

dbConnection.createDB()

dbConnection.disconnect()