import sqlite3
from sqlite3 import Connection, Error


DEFAULT_DATABASE = "sqlitedatabase.db"


class DatabaseManager:
    """Class to manage data stored in an SQLite database"""
    def __init__(self, db=DEFAULT_DATABASE) -> None:
        self.db = db
        self.connection = self.create_connection()


    def create_connection(self) -> Connection:
        """Open and return Connection to the SQLite database."""
        try:
            return sqlite3.connect(self.db)
        except Error as e:
            print("Error connecting to database: ", e)


    def close_connection(self):
        """Close the Connection to the database"""
        try:
            self.connection.close()
        except Error as e:
            print("Error closing connection to database: ", e)


    def get_all_data(self):
        print("I'm talking to the database right now....")