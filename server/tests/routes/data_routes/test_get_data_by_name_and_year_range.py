"""Module for testing the get by year range endpoint"""

from tests.temp_database_setup import TempDatabaseSetup


class TestGetByNameAndYear(TempDatabaseSetup):
    """
    A class that contains methods that test the implementation of method:
    get_data_by_name_and_year()
    """

    def test_get_data(self, client):
        """
        A simple test that takes exactly 1 entry from the server and see if the items are correct
        """
        name = "Canada"
        
        # Initialize parameters to be sent to the server
        name = "Canada"
        start_date = 2001
        end_date = 2001

        # The expected undernourishment value
        expected_value = 2.5

        res = client.get(f'/data/{name}/years?from={start_date}&to={end_date}')
        data = res.get_json()['data']

        assert res.status_code == 200
        for row in data:
            assert row['year'] >= start_date
            assert row['year'] <= end_date

            
    def test_invalid_name(self, client):
        """
        Test that the endpoint doesn't crash with an invalid name
        that isn't in the table.
        """
        
        expected_error_message = "valid parameters <name>, <from> and <to> are required in the query string"
        name = "Canadaa"
        start_date = 2001
        end_date = 2002
        res = client.get(f'/data/{name}/years?from={start_date}&to={end_date}')

        assert res.status_code == 500

    # Remaining tests are the same as those in test_get_by_year_range()
    def test_valid_year_range(self, client):
        """Test that the endpoint returns correct data when given a valid year range"""
        name = "Canada"
        start_date = 2001
        end_date = 2002
        res = client.get(f'/data/{name}/years?from={start_date}&to={end_date}')
        data = res.get_json()['data']

        assert res.status_code == 200
        for row in data:
            assert row['year'] >= start_date
            assert row['year'] <= end_date

    def test_single_year_range(self, client):
        """Test that the endpoint returns correct data when the year range is a single value"""
        name = "Canada"
        start_date = 2001
        res = client.get(f'/data/{name}/years?from={start_date}&to={start_date}')
        data = res.get_json()['data']

        assert res.status_code == 200
        for row in data:
            assert row['year'] == start_date

    def test_invalid_year_range(self, client):
        """Test that the endpoint returns correct data when the year range is invalid"""
        name = "Canada"
        start_date = 2001
        end_date = 2000
        res = client.get(f'/data/{name}/years?from={start_date}&to={end_date}')
        data = res.get_json()['data']

        assert data == []
        assert res.status_code == 200

    def test_negative_years(self, client):
        """Test that the endpoint returns correct data when the given years are negative"""
        name = "Canada"
        start_date = -1
        end_date = -1
        expected_error_message = '<from> and <to> must be valid years (non-negative integers)'
        res = client.get(f'/data/{name}/years?from={start_date}&to={end_date}')
        error_message = res.get_json()['error']['msg']

        assert res.status_code == 400
        assert error_message == expected_error_message

    def test_strings_as_years(self, client):
        """Test that the endpoint returns correct data when the given years are strings"""
        name = "Canada"
        start_date = 'start'
        end_date = 'end'
        expected_error_message = '<from> and <to> must be valid years (non-negative integers)'
        res = client.get(f'/data/{name}/years?from={start_date}&to={end_date}')
        error_message = res.get_json()['error']['msg']

        assert res.status_code == 400
        assert error_message == expected_error_message

    def test_float_as_years(self, client):
        """Test that the endpoint returns correct data when the given years are floats"""
        name = "Canada"
        start_date = 2000.1
        end_date = 2002.1
        expected_error_message = '<from> and <to> must be valid years (non-negative integers)'
        res = client.get(f'/data/{name}/years?from={start_date}&to={end_date}')
        error_message = res.get_json()['error']['msg']

        assert res.status_code == 400
        assert error_message == expected_error_message

    def test_database_failure(self, client):
        """Test that a correct error message is return when the database fails"""
        name = "Canada"
        self.close_db()
        start_date = 2001
        end_date = 2001
        expected_error_message = 'Error fetching data:'
        res = client.get(f'/data/{name}/years?from={start_date}&to={end_date}')
        error_message = res.get_json(
        )['error']['msg'][0: len(expected_error_message)]

        assert res.status_code == 500
        assert error_message == expected_error_message