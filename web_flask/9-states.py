#!/usr/bin/python3
"""Flask app"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def resetDb(self):
    """Method to reset database"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Routing method to display states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_state(id):
    """Routing method to display cities of a state"""
    states = storage.all(State)
    key = "{}.{}".format(State.__name__, id)
    state = states.get(key) if key in states else None
    return render_template('9-states.html', state=state, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
