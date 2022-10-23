"""Module containing Classes and functions relating to managing
the database."""

import sqlite3
from sqlite3 import Connection, Error
from dataclasses import dataclass
from models.rowdata import RowData
import pandas as pd


DEFAULT_DATABASE = 'sqlitedatabase.db'

@dataclass
class Table:
    """Class to hold column and table names of the table in the database"""
    NAME = 'data'
    COLUMN_ENTITY = 'entity'
    COLUMN_YEAR = 'year'
    COLUMN_PREVALENCE = 'prevalence'


class DatabaseManager:
    """Class to manage data stored in an SQLite database"""
    def __init__(self, database=DEFAULT_DATABASE) -> None:
        self.database = database
        self.connection = self.create_connection()


    def create_connection(self) -> Connection:
        """Open and return Connection to the SQLite database."""
        try:
            return sqlite3.connect(self.database)
        except Error as error:
            print('Error connecting to database: ', error)
            return None


    def close_connection(self):
        """Close the Connection to the database"""
        try:
            self.connection.close()
        except Error as error:
            print('Error closing connection to database: ', error)


    def import_dataset(self, path: str) -> None:
        """Imports dataset specified by path and adds it to self.database if it doesn't already
        contain data.

        Assume the dataset is a csv of the form: Country, Country-code, year, prevalence.

        Raises sqlite3.Error, FileNotFoundError, IOError, ValueError.
        """
        try:
            if self.table_exists():
                return # Table already exists, no need to import again
        except Error as error:
            print(f'Error fetching data: {error}')
            raise Error from error

        try:
            dataframe = pd.read_csv(path,
                                    header=0,
                                    usecols=[0,2,3],
                                    names=[
                                        Table.COLUMN_ENTITY,
                                        Table.COLUMN_YEAR,
                                        Table.COLUMN_PREVALENCE])
        except FileNotFoundError as error:
            print(f'Could not find valid dataset file from {path}: {error}')
            raise FileNotFoundError from error
        except IOError as error:
            print(f'Error reading from {path}: {error}')
            raise IOError from error

        try:
            dataframe.to_sql(Table.NAME, self.connection, index=False)
        except ValueError as error:
            print(f'Error importing dataset into database: {error}')
            raise ValueError from error


    def table_exists(self) -> bool:
        """Returns whether the dataset already has a table in the database.
        Raises sqlite3.Error."""
        try:
            cur = self.connection.cursor()
            query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{Table.NAME}'"
            cur.execute(query)
            rows = cur.fetchall()
            return rows != []
        except Error as error:
            raise Error from error


    def update_dataset(self, path: str) -> None:
        """Imports dataset specified by path and adds it to self.database or replaces it if
        it already exists.

        Assume the dataset is a csv of the form: Country, Country-code, year, prevalence.

        Raises FileNotFoundError, IOError, ValueError.
        """
        try:
            dataframe = pd.read_csv(path,
                                    header=0,
                                    usecols=[0,2,3],
                                    names=[
                                        Table.COLUMN_ENTITY,
                                        Table.COLUMN_YEAR,
                                        Table.COLUMN_PREVALENCE])
        except FileNotFoundError as error:
            print(f'Could not find valid dataset file from {path}: {error}')
            raise FileNotFoundError from error
        except IOError as error:
            print(f'Error reading from {path}: {error}')
            raise IOError from error

        try:
            dataframe.to_sql(Table.NAME, self.connection, if_exists='replace', index=False)
        except ValueError as error:
            print(f'Error updating dataset into database: {error}')
            raise ValueError from error


    def get_all_data(self) -> list:
        """Returns a list of RowData objects for each of the entries of the data in the database"""
        cur = self.connection.cursor()
        cur.execute(f'SELECT * FROM {Table.NAME}')

        rows = cur.fetchall()
        cur.close()

        return [RowData(row[0], row[1], row[2]) for row in rows]


    def get_prevalence(self, entity: str, year: int) -> float:
        """Returns the prevalence of the given entity at the given year.
        Returns None if there are no matches for the given entity and year.
        """
        params = (entity, year)
        try:
            cur = self.connection.cursor()
            query = f'SELECT prevalence FROM {Table.NAME} WHERE \
                {Table.COLUMN_ENTITY}=? AND {Table.COLUMN_YEAR}=?'
            cur.execute(query, params)
            result = cur.fetchone()
            cur.close()
            return result[0]
        except Error as error:
            print('Error fetching data: ', error)
            return None
