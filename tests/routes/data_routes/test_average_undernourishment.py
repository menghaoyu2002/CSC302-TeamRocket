"""Module for testing the average undernourishment endpoint"""


from tests.temp_database_setup import TempDatabaseSetup


class TestAverageUndernourishment(TempDatabaseSetup):
    """Class for testing the get_average_undernourishment_by_name endpoint"""

    def test_get_average_undernourishment_by_lower_name(self, client):
        """Tests get_average_undernourishment_by_name() to return correct average when
        name is lowercase
        """
        res = client.get('/data/world/average')
        assert 10.168420992399517 == res.get_json()['data']['average']
        assert res.status_code == 200

    def test_get_average_undernourishment_by_case_insensitive_name(self, client):
        """Tests get_average_undernourishment_by_name() to return correct average
        when the name is upper and lower case.
        """
        res = client.get('/data/wOrLd/average')
        assert 10.168420992399517 == res.get_json()['data']['average']
        assert res.status_code == 200

    def test_get_average_undernourishment_by_name_none(self, client):
        """Tests get_average_undernourishment_by_name() to return error when name
        doesn't exist."""
        res = client.get('/data/Lalaland/average')
        assert res.status_code == 404
