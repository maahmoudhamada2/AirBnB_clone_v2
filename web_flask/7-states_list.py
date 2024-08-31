#!/usr/bin/python3
"""States list"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def resetDB(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """Routing method to get all state from a db"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
