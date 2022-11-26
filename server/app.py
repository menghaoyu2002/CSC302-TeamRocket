"""
the main application
"""
import logging
from pathlib import Path
from sqlite3 import Error
import traceback
from flask import Flask
from flask_cors import CORS
from constants import DATASET_PATH, DEFAULT_DATABASE
from databasemanager import DatabaseManager
from routes.data_route import data_blueprint
from routes.logging_route import logging_blueprint


def create_app(test_config=None):
    """App factory"""

    app = Flask(__name__)

    # initialize logger
    gunicorn_error_logger = logging.getLogger('gunicorn.error')
    app.logger = logging.getLogger()
    app.logger.handlers.extend(gunicorn_error_logger.handlers)
    app.logger.setLevel(gunicorn_error_logger.level)

    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=DEFAULT_DATABASE,
    )

    if test_config is not None:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        db_manager = DatabaseManager(app.config['DATABASE'])
        path = Path(__file__).parent / DATASET_PATH
        db_manager.import_dataset(path)
        db_manager.close_connection()
    except Error as error:
        app.logger.fatal(
            'UNABLE TO INITIALIZE DATABASE: error_message=%s traceback=%s',
            error,
            traceback.format_exc()
        )

    app.register_blueprint(logging_blueprint, url_prefix='/logger')
    app.register_blueprint(data_blueprint, url_prefix='/data')

    return app
