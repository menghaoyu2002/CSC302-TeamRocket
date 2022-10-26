"""
The API route handling database/data operations
"""

from sqlite3 import Error
from flask import Blueprint, current_app, request

from databasemanager import DatabaseManager

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route('/<string:name>', methods=["GET"])
def get_undernourishment_by_name(name):
    """Return all data for the given name"""
    try:
        db_manager = DatabaseManager(current_app.config['DATABASE'])
        data = db_manager.get_data_by_name(name.lower())
        db_manager.close_connection()
        if len(data) == 0:
            return {
                'error': {
                    'msg': 'No entry with the name ' + name
                }
            }, 404
        return {'data': data}, 200
    except Error as error:
        return {
            'error': {
                'msg': f'Error fetching data: {error}'
            }
        }, 500


@data_blueprint.route("/<string:name>/average", methods=["GET"])
def get_average_undernourishment_by_name(name):
    """Return the average undernourishment for the given country"""
    db_manager = DatabaseManager(current_app.config['DATABASE'])
    try:
        data = db_manager.get_data_by_name(name.lower())
        db_manager.close_connection()
    except Error as error:
        return {
            'error': {
                'msg': f'Error fetching data: {error}'
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


@data_blueprint.route('/years', methods=['GET'])
def get_by_year_range():
    start_year = request.args.get('from')
    end_year = request.args.get('to')

    if not start_year or not end_year:
        return {
            'error': {
                'msg': 'parameters <from> and <to> are required in the query string'
            }
        }, 400

    try:
        db_manager = DatabaseManager(current_app.config['DATABASE'])
        data = db_manager.get_data_from_year_range(start_year, end_year)
        db_manager.close_connection()
        return {'data': data}, 200
    except Error as error:
        return {
            'error': {
                'msg': f'Error fetching data: {error}'
            }
        }, 500
