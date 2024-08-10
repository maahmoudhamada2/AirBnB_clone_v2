#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True


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


@app.route("/number/<int:n>")
def number_route(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
