from flask import Flask

app = Flask(__name__)


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
