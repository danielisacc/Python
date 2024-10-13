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
#### Modules
- OutputStream
    - Sub-package designed to offer different OutputStream classes.
- APIHandler.py
    - Module designed to handle API requests, data parsing, and sending data to sources such as DataModeling Objects and OutputStreams.
- DataModeling.py
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