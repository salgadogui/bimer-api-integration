from sqlalchemy import create_engine, Integer
import os


class MigrationService:
    def __init__(self):
        self.engine = create_engine(
            f'postgresql://{os.environ["PSQL_USERNAME"]}:{os.environ["PSQL_PASSWORD"]}@localhost:{os.environ["PSQL_PORT"]}/{os.environ["PSQL_DATABASE"]}'
        )

    def migrateData(self, df, table):
        df.to_sql(f'{table}', self.engine, index=False, if_exists='replace', dtype={'id': Integer})
        print("Migration successful!")