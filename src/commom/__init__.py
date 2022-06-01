import sqlite3 as sq


def create_connection(table_name):
    try:
        conn = sq.connect(f"{table_name}.sqlite")
        return conn
    except Exception as err:
        print("Failed to connect with sqlite", {"error": err})
