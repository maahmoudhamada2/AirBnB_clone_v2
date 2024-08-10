#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

state_objs = storage.all(State)

app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """Method to close current session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Method to display some data"""
    return render_template('7-states_list.html', state_objs=state_objs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
