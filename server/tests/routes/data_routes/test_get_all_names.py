"""Module for testing the get all names endpoint"""

from databasemanager import DatabaseManager
from tests.temp_database_setup import TempDatabaseSetup

NUMBER_OF_ENTRIES = 176


class TestGetAllNames(TempDatabaseSetup):
    """class for testing the get all names endpoint"""

    def test_correct_number_of_names(self, client):
        """Test that the returned data has the correct number of entries"""
        res = client.get('/data/names')
        names = res.get_json()['data']
        assert len(names) == NUMBER_OF_ENTRIES

    def test_names_are_distinct(self, client):
        """Test that the all names in the return data are distinct"""
        res = client.get('/data/names')
        names = res.get_json()['data']
        assert len(names) == len(set(names))

    def test_queries_passed(self, client):
        """Test that the endpoint is unaffected by any query parameters"""
        query_res = client.get('/data/names?query=here')
        names_with_query = query_res.get_json()['data']
        res = client.get('/data/names')
        names = res.get_json()['data']
        assert names == names_with_query

    def test_all_valid_names(self, client):
        """Test that all names are valid and are in the database"""
        res = client.get('/data/names')
        names = res.get_json()['data']

        db_manager = DatabaseManager()
        for name in names:
            assert len(db_manager.get_data_by_name(name)) > 0

        db_manager.close_connection()

    def test_database_failure(self, client):
        """Test that the endpoint handles database failure"""
        self.close_db()
        res = client.get('/data/names')
        expected_error_message = 'Error fetching data:'
        error_message = res.get_json(
        )['error']['msg'][0: len(expected_error_message)]
        assert error_message == expected_error_message
