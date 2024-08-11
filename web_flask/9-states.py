#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def reset_session(self):
    """Method to reset current session of db"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states_display():
    """Method to return states html page"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>")
def state_by_id(id):
    """Method to display city of specific state"""
    key = "State.{}".format(id)
    states = storage.all(State)
    return render_template('9-states.html', states=states, key=key)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
