"""Module for testing the average undernourishment endpoint"""

import os
import tempfile
import pytest
from app import app


class TestAverageUndernourishment:
    """Class for testing the get_average_undernourishment_by_name endpoint"""
    @pytest.fixture
    def client(self):
        """Fixture to be called before each test to set up app interface"""
        db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True

        with app.test_client() as client:
            yield client

        os.close(db_fd)
        os.unlink(app.config['DATABASE'])

    def test_get_average_undernourishment_by_name(self, client):
        """Tests get_average_undernourishment_by_name() to return correct average."""
        res = client.get('/World/average').get_json()
        print(res)
        assert 10.168420992399517 == res['data']['average']

    def test_get_average_undernourishment_by_name_none(self, client):
        """Tests get_average_undernourishment_by_name() to return correct average when name
        doesn't exist."""
        res = client.get('/Lalaland/average').get_json()
        assert 0 == res['data']['average']
