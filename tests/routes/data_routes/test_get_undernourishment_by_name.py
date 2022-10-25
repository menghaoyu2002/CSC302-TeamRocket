"""Module for testing the get undernourishment by name endpoint"""

from tests.TempDatabaseSetup import TempDatabaseSetup


class TestGetUndernourishmentByName(TempDatabaseSetup):
    """Test the get undernourishment by name endpoint"""

    def test_get_canada_undernourishment(self, client):
        """Test that the get undernourishment endpoint returns the correct value for Canada"""
        res = client.get('/data/canada')

        data = res.get_json()['data']
        assert len(data) == 19
        assert res.status_code == 200
        expected_year = 2001
        for row in data:
            assert row['name'] == 'canada'
            assert row['undernourishment'] == 2.5
            assert row['year'] == expected_year
            expected_year += 1

    def test_get_nonexistent_undernourishment(self, client):
        res = client.get('/data/disneyland')
        assert res.status_code == 404
        expected_error_msg = 'No entry with the name disneyland'
        actual_error_msg = res.get_json(
        )['error']['msg'][0:len(expected_error_msg)]
        assert actual_error_msg == expected_error_msg

    def test_get_undernourishment_with_db_error(self, client):
        self.close_db()
        res = client.get('/data/disneyland')
        assert res.status_code == 500
        expected_error_msg = 'Error fetching data:'
        actual_error_msg = res.get_json(
        )['error']['msg'][0:len(expected_error_msg)]

        assert actual_error_msg == expected_error_msg
