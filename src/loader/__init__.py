import sqlite3 as sq
from src.commom import create_connection


class Loader:
    def __init__(self):
        self.TABLE_NAME = "person_data"
        self.conn = create_connection(self.TABLE_NAME)

    def load_data(self, data):
        try:
            data.to_sql(self.TABLE_NAME, self.conn, if_exists="replace", index=False)
            self.conn.close()
            print("Data loaded with success")
        except Exception as err:
            print("Failed to load data", {"error": err})
