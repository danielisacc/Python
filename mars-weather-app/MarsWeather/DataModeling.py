"""Module designed to recieve data from the DB,
generate DataModels, then output the Data Models to an OutputStream."""

import pandas as pd
from OutputStream.DBStream import DBStream

class DataModel():
    def __init__(self, connection: DBStream) -> None:
        pass