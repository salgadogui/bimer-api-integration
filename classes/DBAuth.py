from dotenv import load_dotenv
import pyodbc
import os

load_dotenv()

class DBAuth:
    def __init__(self):
        self.connection_string = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            f'SERVER={os.environ['MSSQL_DB_SERVER']};'
            f'DATABASE={os.environ['MSSQL_DB_PRODUCTION_DATABASE']};'
            'Trusted_Connection=yes;'
        )

    def connectToDb(self):
        try:
            connection = pyodbc.connect(self.connection_string)
            print("Connection successful!\n")    

            return connection

        except pyodbc.Error as ex:
            sqlstate = ex.args[1]
            print(f"Connection failed. Error: {sqlstate}")