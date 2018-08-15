#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


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
