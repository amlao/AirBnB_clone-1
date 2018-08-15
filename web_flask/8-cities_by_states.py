#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """
       display “Hello HBNB!”
    """
    return "Hello HBNB!"

@app.route('/', strict_slashes=False)
def hbnb():
    """
       display “HBNB”
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
       display “C ” followed by the value of the text variable
    """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def monty(text="is cool"):
    """
       display “Python ”, followed by the value of the text variable
    """
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    """
       display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n=None):
    B"""
       display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """
       display a HTML page only if n is an integer
    """
    if n % 2 == 0:
        nan = "even"
    else:
        nan = "odd"
    return render_template('6-number_odd_or_even.html', n=n, nan=nan)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
       the list of all State objects present in DBStorage
    """
    return render_template('7-states_list.html', state_objs=storage.all(State))

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
       the list of City objects linked to the State
    """
    return render_template('8-cities_by_states.html',
                           city_objs=storage.all(State))

@app.teardown_appcontext
def teardown(exception):
    """
       remove the current SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
