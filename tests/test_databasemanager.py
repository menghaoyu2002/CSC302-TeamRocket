"""Module for testing the DatabaseManager."""

from pathlib import Path
from models.rowdata import RowData
from databasemanager import DatabaseManager
from constants import DATASET_PATH

class TestDatabaseManager:
    """Class for testing DatabaseManager."""
    db_manager = DatabaseManager()

    def test_import(self):
        """Test import_dataset() does not raise any exceptions."""
        path = Path(__file__).parent / f'../app/{DATASET_PATH}'
        try:
            self.db_manager.import_dataset(path)
        except:
            assert False

    def test_update(self):
        """Test update_dataset() does not raise any exceptions."""
        path = Path(__file__).parent / f'../app/{DATASET_PATH}'
        try:
            self.db_manager.update_dataset(path)
        except:
            assert False

    def test_update_fail(self):
        """Test update_dataset() does not raises exception on input of an invalid path."""
        try:
            self.db_manager.update_dataset('somepath')
        except FileNotFoundError:
            assert True

    def test_get_prevalence_one(self):
        """Test get_prevalence() returns the correct value from the database."""
        assert self.db_manager.get_prevalence('Afghanistan', 2004) == 38.0

    def test_get_prevalence_none(self):
        """Test get_prevalence() returns None if there are no matches."""
        assert self.db_manager.get_prevalence('Lalaland', 2004) is None

    def test_get_all_data(self):
        """Test get_all_data() returns a list of RowData from the database."""
        data = self.db_manager.get_all_data()
        assert isinstance(data, list)
        assert data[0] == RowData('Afghanistan', 2001, 47.79999923706055)
