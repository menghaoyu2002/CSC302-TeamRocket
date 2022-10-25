"""
The API route handling database/data operations
"""
from sqlite3 import Error
from flask import Blueprint, current_app

from databasemanager import DatabaseManager

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route("/<string:name>/average", methods=["GET"])
def get_average_undernourishment_by_name(name):
    """Return the average undernourishment for the given country"""
    db_manager = DatabaseManager(current_app.config['DATABASE'])
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
