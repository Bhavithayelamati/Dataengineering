import pandas as pd
import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect

class DatabaseConnector:

    def __init__(self):
        pass

    def read_db_creds(self, name):
        with open(name, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def init_db_engine(self, cred):
        engine = create_engine(
            f"{'postgresql'}+{'psycopg2'}://{cred['RDS_USER']}:{cred['RDS_PASSWORD']}@{cred['RDS_HOST']}:{cred['RDS_PORT']}/{cred['RDS_DATABASE']}")
        return engine

    def list_db_tables(self, engine):
        inspector = inspect(engine)
        return inspector.get_table_names()

    def upload_to_db(self, df, name, engine):
        df.to_sql(name, engine, if_exists='replace')
'''
if __name__ == '__main__':
    db = DatabaseConnector()
    engine = db.init_db_engine(db.read_db_creds("db_creds.yaml"))
    engine.connect()
    print("Hi")
    print(engine)
    tables_list = db.list_db_tables(engine)
    print(tables_list)
    with engine.begin() as conn:
        table = pd.read_sql_table(tables_list[1], con=conn)
    print(table)
'''
if __name__ == '__main__':
    db = DatabaseConnector()
    engine = db.init_db_engine(db.read_db_creds("db_creds.yaml"))
    engine.connect()
    print("Hi")
    print(engine)
    tables_list = db.list_db_tables(engine)
    print(tables_list)

    for table_name in tables_list:
        with engine.begin() as conn:
            table = pd.read_sql_table(table_name, con=conn)
            # Save each table as a separate CSV file
            csv_filename = f"{table_name}.csv"
            table.to_csv(csv_filename, index=False)
            print(f"Table '{table_name}' saved to '{csv_filename}'")
