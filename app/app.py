"""
the main application
"""

from pathlib import Path
from flask import Flask, request
from constants import DATASET_PATH, DEFAULT_DATABASE
from databasemanager import DatabaseManager

app = Flask(__name__)
app.config['DATABASE'] = DEFAULT_DATABASE

db_manager = DatabaseManager(app.config['DATABASE'])
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


@app.route("/<string:name>/average", methods=["GET"])
def get_average_undernourishment_by_name(name):
    """Return the average undernourishment for the given country"""
    data = db_manager.get_data_by_name(name)

    undernourishments = [row_data.undernourishment for row_data in data]

    return {
        'data': {
            'average': sum(undernourishments) / len(undernourishments) \
                if undernourishments != [] else 0
        }
    }, 200
