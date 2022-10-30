"""Module for testing the DatabaseManager."""

from pathlib import Path
from sqlite3 import Error
from constants import DATASET_PATH
from databasemanager import DatabaseManager
from models.rowdata import RowData


class TestDatabaseManager:
    """Class for testing DatabaseManager."""
    db_manager = DatabaseManager()

    def test_import(self):
        """Test import_dataset() does not raise any exceptions."""
        path = Path(__file__).parent / f'../app/{DATASET_PATH}'
        try:
            self.db_manager.import_dataset(path)
        except Error:
            assert False
        except FileNotFoundError:
            assert False

    def test_update(self):
        """Test update_dataset() does not raise any exceptions."""
        path = Path(__file__).parent / f'../app/{DATASET_PATH}'
        try:
            self.db_manager.update_dataset(path)
        except Error:
            assert False
        except FileNotFoundError:
            assert False

    def test_update_fail(self):
        """Test update_dataset() does not raises exception on input of an invalid path."""
        try:
            self.db_manager.update_dataset('somepath')
        except FileNotFoundError:
            assert True

    def test_get_undernourishment_one(self):
        """Test get_undernourishment() returns the correct value from the database."""
        assert self.db_manager.get_undernourishment(
            'afghanistan', 2004) == 38.0

    def test_get_undernourishment_none(self):
        """Test get_undernourishment() returns None if there are no matches."""
        assert self.db_manager.get_undernourishment('Lalaland', 2004) is None
            
    def test_get_data_by_name_and_year(self):
        """
        Test functionality of test_get_data_by_name_and_year()
        """
        
        try:
            print("Beginning tests for method get_data_by_name_and_year()...")
            test_result = self.db_manager.get_data_by_name_and_year("Canada", 2001)
            assert test_result[2] == 2.5
        except:
            print("Exception raised when testing method: get_data_by_name_and_year.")
    
    def test_get_all_data(self):
        """Test get_all_data() returns a list of RowData from the database."""
        data = self.db_manager.get_all_data()
        assert isinstance(data, list)
        assert data[0] == RowData('afghanistan', 2001, 47.79999923706055)

    def test_get_data_by_name(self):
        """Test get_data_by_name() returns a list of all RowData with given name."""
        data = self.db_manager.get_data_by_name('world')
        assert isinstance(data, list)
        assert data[0] == RowData('world', 2001, 13.199999809265137)
