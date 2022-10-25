"""The base Class for testing any functionality requiring the database"""

import os
import tempfile
import pytest

from app import create_app


class TempDatabaseSetup:
    """The base Class for testing any functionality requiring the database"""

    def __init__(self) -> None:
        self.db_fd = None
        self.db_path = None

    @pytest.fixture
    def client(self):
        """Fixture to be called before each test to set up app interface"""
        self.db_fd, self.db_path = tempfile.mkstemp()

        app = create_app({
            'TESTING': True,
            'DATABASE': self.db_path,
        })

        with app.test_client() as client:
            yield client

        if self.db_fd and self.db_path:
            self.close_db()

    def close_db(self):
        """Close the temporary database"""
        os.close(self.db_fd)
        os.unlink(self.db_path)
        self.db_fd = None
        self.db_path = None
