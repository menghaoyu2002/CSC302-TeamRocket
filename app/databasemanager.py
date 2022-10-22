import pandas as pd
import sqlite3
from sqlite3 import Connection, Error
from dataclasses import dataclass


DEFAULT_DATABASE = 'sqlitedatabase.db'

@dataclass
class Table:
    NAME = 'data'
    COLUMN_ENTITY = 'entity'
    COLUMN_YEAR = 'year'
    COLUMN_PREVALENCE = 'prevalence'




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
            print('Error connecting to database: ', e)


    def close_connection(self):
        """Close the Connection to the database"""
        try:
            self.connection.close()
        except Error as e:
            print('Error closing connection to database: ', e)


    def import_dataset(self, path: str):
        """Imports dataset specified by path and adds it to self.db.
        Returns whether data was successfully imported into self.db.

        Assume the dataset is a csv of the form: Country, Country-code, year, prevalence.
        """
        try:
            df = pd.read_csv(path, header=0, usecols=[0,2,3], names=[Table.COLUMN_ENTITY, Table.COLUMN_YEAR, Table.COLUMN_PREVALENCE])
        except FileNotFoundError:
            print(f'Could not find valid dataset file from {path}')
            return False
        except:
            print(f'Error reading from {path}')
            return False

        try:
            df.to_sql(Table.NAME, self.connection, if_exists='replace', index=False)
        except:
            print('Error importing dataset into database')
            return False

        return True


    def get_all_data(self):
        """Prints the first 10 entries of the data in the database"""
        cur = self.connection.cursor()
        cur.execute(f'SELECT * FROM {Table.NAME}')

        rows = cur.fetchall()

        for i in range(10):
            print(rows[i])

        cur.close()


    def get_prevalence(self, entity: str, year: int) -> float:
        """Returns the prevalence of the given entity at the given year.
        
        Returns None if there are no matches for the given entity and year.
        """
        params = (entity, year)
        try:
            cur = self.connection.cursor()
            cur.execute(f'SELECT prevalence FROM {Table.NAME} WHERE {Table.COLUMN_ENTITY}=? AND {Table.COLUMN_YEAR}=?', params)
            result = cur.fetchone()
            cur.close()
            return result[0]
        except Error as e:
            print('Error fetching data: ', e)
            return None