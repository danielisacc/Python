from MarsWeather.OutputStream.DBConnections.SQLite3Connection import SQLiteConnection
from MarsWeather import APIHandler
from MarsWeather import DataModeling
# Connect to the API and load JSON response into data variable
# api = APIHandler.APIHandler()
# api.connect()
# data = api.getJSON()

# Create DB connection, createDB will create missing tables
dbConnection = SQLiteConnection()
model = DataModeling.DataModel(dbConnection)
# dbConnection.createDB()

# Send JSON API data into the DB
# dbConnection.insert(data)

# Disconnect from the DB commiting before closing connection.
dbConnection.disconnect()
