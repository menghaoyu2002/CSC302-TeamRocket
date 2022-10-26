from tests.temp_database_setup import TempDatabaseSetup


class TestGetByYearRange(TempDatabaseSetup):
    """Test the get data by year range endpoint"""

    def test_valid_year_range(self, client):
        start_date = 2001
        end_date = 2002
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        data = res.get_json()['data']

        assert res.status_code == 200
        for row in data:
            assert row['year'] >= start_date
            assert row['year'] <= end_date

    def test_single_year_range(self, client):
        start_date = 2001
        res = client.get(f'/data/years?from={start_date}&to={start_date}')
        data = res.get_json()['data']

        assert res.status_code == 200
        for row in data:
            assert row['year'] == start_date

    def test_invalid_year_range(self, client):
        start_date = 2001
        end_date = 2000
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        data = res.get_json()['data']

        assert data == []
        assert res.status_code == 200

    def test_negative_years(self, client):
        start_date = -1
        end_date = -1
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        data = res.get_json()['data']

        assert data == []
        assert res.status_code == 200

    def test_strings_as_years(self, client):
        start_date = 'start'
        end_date = 'end'
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        data = res.get_json()['data']

        assert data == []
        assert res.status_code == 200

    def test_database_failure(self, client):
        self.close_db()
        start_date = 2001
        end_date = 2001
        res = client.get(f'/data/years?from={start_date}&to={end_date}')
        expected_error_message = 'Error fetching data:'
        error_message = res.get_json(
        )['error']['msg'][0: len(expected_error_message)]

        assert res.status_code == 500
        assert error_message == expected_error_message
