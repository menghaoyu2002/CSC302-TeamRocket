"""
the main application
"""

from flask import Flask, request
from pathlib import Path
from constants import DATASET_PATH
from databasemanager import DatabaseManager

app = Flask(__name__)

db_manager = DatabaseManager()
path = Path(__file__).parent / DATASET_PATH
db_manager.import_dataset(path)


@app.route("/")
def index():
    """
    Create the index for the website.
    """
    return "<p>Index Page of the website</p>"


@app.route("/home")
def home_page():
    """
    Create the home page for the website.
    """
    return "<p>This is the home page! Make sure the other routes are in different files!</p>"


@app.route("/data/average", methods=["GET"])
def get_average_undernourishment_by_name():
    """Return the average undernourishment for the given country"""
    args = request.args
    name = args.get('name', default='World')

    data = db_manager.get_data_by_name(name)

    undernourishments = [row_data.undernourishment for row_data in data]

    return {
        'data': {
            'average': sum(undernourishments) / len(undernourishments) \
                if undernourishments != [] else 0
        }
    }, 200
