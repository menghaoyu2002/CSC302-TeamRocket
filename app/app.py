"""
the main application
"""

from pathlib import Path
from flask import Flask
from constants import DATASET_PATH, DEFAULT_DATABASE
from databasemanager import DatabaseManager
from routes.data_route import data_blueprint


def create_app(test_config=None):
    """App factory"""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=DEFAULT_DATABASE,
    )

    if test_config is not None:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    db_manager = DatabaseManager(app.config['DATABASE'])
    path = Path(__file__).parent / DATASET_PATH
    db_manager.import_dataset(path)
    db_manager.close_connection()

    app.register_blueprint(data_blueprint, url_prefix='/data')

    return app
