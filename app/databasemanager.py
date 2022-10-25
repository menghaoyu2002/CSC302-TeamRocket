"""Module containing Classes and functions relating to managing
the database."""

import sqlite3
from dataclasses import dataclass
from typing import List, Optional

from models.rowdata import RowData
from constants import DEFAULT_DATABASE
import pandas as pd


@dataclass
class Table:
    """Class to hold column and table names of the table in the database"""
    NAME = 'data'
    COLUMN_ENTITY = 'entity'
    COLUMN_YEAR = 'year'
    COLUMN_UNDERNOURISHMENT = 'undernourishment'


class DatabaseManager:
    """Class to manage data stored in an SQLite database"""

    def __init__(self, database=DEFAULT_DATABASE) -> None:
        self.database = database
        self.connection = None
        self.create_connection()

    def create_connection(self) -> None:
        """Opens a connection to the SQLite database."""
        self.connection = sqlite3.connect(
            self.database, check_same_thread=False)

    def close_connection(self) -> None:
        """Close the Connection to the database"""
        self.connection.close()

    def import_dataset(self, path: str) -> None:
        """Imports dataset specified by path and adds it to self.database if it doesn't already
        contain data.

        Assume the dataset is a csv of the form: Country, Country-code, year, prevalence.
        """
        if self.table_exists():
            return  # Table already exists, no need to import again

        dataframe = self._read_dataset(path)

        dataframe.to_sql(Table.NAME, self.connection, index=False)

    def table_exists(self) -> bool:
        """Returns whether the dataset already has a table in the database."""
        cur = self.connection.cursor()
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{Table.NAME}'"
        rows = cur.execute(query).fetchall()
        return rows != []

    def update_dataset(self, path: str) -> None:
        """Imports dataset specified by path and adds it to self.database or replaces it if
        it already exists.

        Assume the dataset is a csv of the form: Country, Country-code, year, prevalence.
        """
        dataframe = self._read_dataset(path)

        dataframe.to_sql(Table.NAME, self.connection,
                         if_exists='replace', index=False)

    def _read_dataset(self, path: str) -> pd.DataFrame:
        """
        Read the dataset into a pandas dataframe
        """
        dataframe = pd.read_csv(path,
                                header=0,
                                usecols=[0, 2, 3],
                                names=[
                                    Table.COLUMN_ENTITY,
                                    Table.COLUMN_YEAR,
                                    Table.COLUMN_UNDERNOURISHMENT]
                                )

        dataframe[Table.COLUMN_ENTITY] = dataframe[Table.COLUMN_ENTITY].str.lower()

        return dataframe

    def get_all_data(self) -> List[RowData]:
        """Returns a list of RowData objects for each of the entries of the data in the database"""
        cur = self.connection.cursor()
        rows = cur.execute(f'SELECT * FROM {Table.NAME}').fetchall()
        cur.close()

        return [RowData(row[0], row[1], row[2]) for row in rows]

    def get_undernourishment(self, entity: str, year: int) -> Optional[float]:
        """Returns the undernourishment of the given entity at the given year.
        Returns None if there are no matches for the given entity and year.
        """
        params = (entity, year)
        cur = self.connection.cursor()
        query = f'SELECT {Table.COLUMN_UNDERNOURISHMENT} FROM {Table.NAME} WHERE \
            {Table.COLUMN_ENTITY}=? AND {Table.COLUMN_YEAR}=?'
        result = cur.execute(query, params).fetchone()
        cur.close()

        return result if result is None else result[0]

    def get_data_by_name(self, name: str) -> List[RowData]:
        """Returns a list of RowData object that have name as their RowData.name."""
        params = (name,)
        cur = self.connection.cursor()
        query = f'SELECT * FROM {Table.NAME} WHERE {Table.COLUMN_ENTITY}=? ORDER BY year'
        result = cur.execute(query, params).fetchall()
        cur.close()

        return [RowData(row[0], row[1], row[2]) for row in result]
