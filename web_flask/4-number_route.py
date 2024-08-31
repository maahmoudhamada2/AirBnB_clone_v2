#!/usr/bin/python3
"""0-hello_route app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """Routing method to return a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Routing method to return a string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_function(text):
    """Routing method to return C string """
    text = 'C ' + text.replace('_', ' ')
    return text


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_function(text="is cool"):
    """Routing method to return python string"""
    text = 'Python ' + text.replace('_', ' ')
    return text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Routing method to return string if n is only a num"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
