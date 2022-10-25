"""Module for testing the average undernourishment endpoint"""

import os
import tempfile
import pytest
from app import create_app


class TestAverageUndernourishment:
    """Class for testing the get_average_undernourishment_by_name endpoint"""

    @pytest.fixture
    def client(self):
        """Fixture to be called before each test to set up app interface"""
        db_fd, db_path = tempfile.mkstemp()

        app = create_app({
            'TESTING': True,
            'DATABASE': db_path,
        })

        with app.test_client() as client:
            yield client

        os.close(db_fd)
        os.unlink(db_path)

    def test_get_average_undernourishment_by_name(self, client):
        """Tests get_average_undernourishment_by_name() to return correct average."""
        res = client.get('/data/World/average')
        assert 10.168420992399517 == res.get_json()['data']['average']
        assert res.status_code == 200

    def test_get_average_undernourishment_by_name_none(self, client):
        """Tests get_average_undernourishment_by_name() to return error when name
        doesn't exist."""
        res = client.get('/data/Lalaland/average')
        assert res.status_code == 404
