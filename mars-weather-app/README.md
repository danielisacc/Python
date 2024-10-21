# Mars Weather App

## Summary
This app is desgined to collect data from NASA's Mars Weather API and output that Data to a source such as a console, website, file system, or even a Website. This app is in development.

## Requirements
- Collect Mars Weather Data
    - Connect to NASA API
    - Authenticate connection
    - Collect data
    - Parse Data
    - Using pandas store data in table
    - return table using pullAPIData()
- Generate Data Models
    - Pull data from DBStream
    - Using pandas and matplotlib create data models
    - Post data to OutputStream
- Output Data to a Source
    - Output to OutputStream Objects
        - ConsoleStream
            - Output lines of data as arrays
        - FileStream
            - Output lines of data to Files
        - DBStream
            - Output elements as rows into DB tables
    - Post to DBStream
        - SQLite
        - SQL*Plus
        - MySQL
- Django as Output

## Packages
### MarsWeather
This package is desgined to collect the data from NASA's API then generate Data Models. This package does have multiple output types designed for testing such as ConsoleStream, but it's main function will be used as a backend for Django to collect data from a DB storing the data.
#### MarsWeather Modules
- [OutputStream](OutputStream)
    - Sub-package designed to offer different OutputStream classes.
- [APIHandler.py](APIHandler)
    - Module designed to handle API requests, data parsing, and sending data to sources such as DataModeling Objects and OutputStreams.
- [DataModeling.py](DataModeling.py)
    - Module designed to recieve data from APIHandler, generate DataModels, then output the Data Models to an OutputStream.
### Django
This package will act as the website manager, calling DBStream data, APIHandler update requests, and DataModeling Objects. The manager will then output the data to a website in a *hopefully* elegant design. Most calls for the MarsWeather Data will actually be to the app.py file to allocate lower level tasks outside django.

## Setting Up Your Enviorment
For security purposes, there are no hard coded API keys. The connect method from the APIHandler class takes one optional paramter called api_key:str. If a key is not provided in the method call, then it will default to an Environement Variable called MARS_WEATHER_API_KEY. This can be set using either the linux terminal or the windows termal as instructed below.

- On Linux
```bash
export MARS_WEATHER_API_KEY=your_api_key_here
```
- On Windows
```bash
set MARS_WEATHER_API_KEY=your_api_key_here
```

## APIHandler
Module of MarsWeather package that is used to connect to NASA's Insight API, then return the json response from the API.
### APIHandler Classes and Methods
- **APIHandler** - The main class of the module used to connect to the API and return the json response.
    - APIHandler() - Constructor of class. When object is initialized, it generates a dictionary of strings used to create the get request (_url, api_key, feedType, ver_).
    - connect() - Used to connect to the API using the api_key retrieved from the enviornemental variable created earlier, or prompting the user to input one. There are no hardcoded keys. _APIKeyError_ raised if invalid key.
    - getJson() - Used to return the API json response if a successful connection was made. If a connection was not created, or the connection was unsuccessful, the _FailedAPIConnection_ error is raised.
- **APIError(_Exception_)** - Acts as the root exception class for API related errors. Inherits from the root Exception class of Python.
- **FailedAPIConnection(_APIError_)** - Designed to trigger when there is a failed connection to the API for any reason. Inherits from root APIError class.
- **APIKeyError(_FailedAPIConnection_)** - Desgined to be raised when an invalid Key is entered into the get request. Inherits from FailedAPIConnection(APIErrors) class, since it is a specific failed connection error.

## OutputStream
A subpackage containing the output options used during developement.
### Subpackages and Modules
- **DBConnection** - Subpackage storing modules for connecting to DB's, creating DB schemas, inserting API JSON values and executing queries.
- **consoleStream.py** - Module used to output the DataModels and raw JSON data to the console.
- **FileStream.py** - Module used to stream the DataModels and raw JSON data into a file.
#### DBConnection Modules
- DBConnection - Abstract class for all DBConnection types to inherit from, outlining different functionalites that DBConnection Classes need to impliment.
    - connect() - Used to connect to the DB.
    - disconnect() - Used to disconnect from the DB
    - execute(str) - Used to execute a single query.
    - insert(dict) - Used to insert the API JSON response into the db.
- MySQLConnection.py - Concrete implimentation of DBConnection abstract class that uses a MySQL DB.
- SQLite3Connection.py - Concrete implimentation of DBConnection abstract class that uses a SQLite3 DB.