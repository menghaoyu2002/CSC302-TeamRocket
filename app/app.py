"""
the main application
"""

from pathlib import Path
from sqlite3 import Error
from flask import Flask
from constants import DATASET_PATH, DEFAULT_DATABASE
from databasemanager import DatabaseManager


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

    @app.route("/<string:name>/average", methods=["GET"])
    def get_average_undernourishment_by_name(name):
        """Return the average undernourishment for the given country"""
        try:
            data = db_manager.get_data_by_name(name.lower())
        except Error as error:
            return {
                'error': {
                    f'Error fetching data: {error}'
                }
            }, 500

        undernourishments = [row_data.undernourishment for row_data in data]

        if undernourishments != []:
            return {
                'data': {
                    'average': sum(undernourishments) / len(undernourishments)
                }
            }, 200

        return {
            'error': 'No data found for name: ' + name
        }, 404

    return app
