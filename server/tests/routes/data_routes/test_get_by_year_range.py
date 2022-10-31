"""Module for testing the get by year range endpoint"""

from tests.temp_database_setup import TempDatabaseSetup


class TestGetByYearRange(TempDatabaseSetup):
    """Test the get data by year range endpoint"""

    def test_valid_year_range(self, client):
        """Test that the endpoint returns correct data when given a valid year range"""
        start_date = 2001
        end_date = 2002
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        data = res.get_json()['data']

        assert res.status_code == 200
        for row in data:
            assert row['year'] >= start_date
            assert row['year'] <= end_date

    def test_single_year_range(self, client):
        """Test that the endpoint returns correct data when the year range is a single value"""
        start_date = 2001
        res = client.get(f'/data/years?from={start_date}&to={start_date}')
        data = res.get_json()['data']

        assert res.status_code == 200
        for row in data:
            assert row['year'] == start_date

    def test_invalid_year_range(self, client):
        """Test that the endpoint returns correct data when the year range is invalid"""
        start_date = 2001
        end_date = 2000
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        data = res.get_json()['data']

        assert data == []
        assert res.status_code == 200

    def test_negative_years(self, client):
        """Test that the endpoint returns correct data when the given years are negative"""
        start_date = -1
        end_date = -1
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        expected_error_message = '<from> and <to> must be valid years (non-negative integers)'
        error_message = res.get_json()['error']['msg']

        assert res.status_code == 400
        assert error_message == expected_error_message

    def test_strings_as_years(self, client):
        """Test that the endpoint returns correct data when the given years are strings"""
        start_date = 'start'
        end_date = 'end'
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        expected_error_message = '<from> and <to> must be valid years (non-negative integers)'
        error_message = res.get_json()['error']['msg']

        assert res.status_code == 400
        assert error_message == expected_error_message

    def test_float_as_years(self, client):
        """Test that the endpoint returns correct data when the given years are floats"""
        start_date = 2000.1
        end_date = 2002.1
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        expected_error_message = '<from> and <to> must be valid years (non-negative integers)'
        error_message = res.get_json()['error']['msg']

        assert res.status_code == 400
        assert error_message == expected_error_message

    def test_database_failure(self, client):
        """Test that a correct error message is return when the database fails"""
        self.close_db()
        start_date = 2001
        end_date = 2001
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        expected_error_message = 'Error fetching data:'
        error_message = res.get_json(
        )['error']['msg'][0: len(expected_error_message)]

        assert res.status_code == 500
        assert error_message == expected_error_message
