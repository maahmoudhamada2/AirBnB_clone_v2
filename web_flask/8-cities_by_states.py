#!/usr/bin/python3
"""Flask app"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def reset_db(self):
    """Method to reset database"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_cities():
    """Routing method to display cities by states"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
