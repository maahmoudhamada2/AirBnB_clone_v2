#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greetings():
    """Method for route path"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    text = 'C' + ' ' + text.replace('_', ' ')
    return "{}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_route(text="is cool"):
    text = 'Python' + ' ' + text.replace('_', ' ')
    return "{}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
