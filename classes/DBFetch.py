from classes.DBAuth import DBAuth
import pandas as pd

class DBFetch:
    def __init__(self, query):
        self.connection = DBAuth().connectToDb
        self.query = query

    def run(self):
        try:
            connection = self.connection()
            cursor = connection.cursor()
            cursor.execute(self.query)            
            fetched_data = cursor.fetchall()
            fetched_data = [tuple(row) for row in fetched_data]
            columns = [column[0] for column in cursor.description]

            df = pd.DataFrame(fetched_data, columns=columns)

            for col in df.select_dtypes(include=['object']).columns:
                df[col] = df[col].str.strip()

            return df
        
        finally:
            if 'connection' in locals() and connection is not None:
                connection.close()
