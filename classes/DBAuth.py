from dotenv import load_dotenv
import os

load_dotenv()

class DBAuth:
    def __init__(self):
        self.connection_string = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            f"SERVER={os.environ['MSSQL_DB_SERVER']};"
            f'DATABASE={os.environ["MSSQL_DB_PRODUCTION_DATABASE"]};'
            'Trusted_Connection=yes;'
        )

    def connectToDb(self):
        print("Database connection bypassed - running in mock mode")
        return None  # Return None instead of attempting a real connection