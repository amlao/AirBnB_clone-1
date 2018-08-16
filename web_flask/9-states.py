#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
       the list of all State objects present in DBStorage
    """
    state_obj = storage.all(State)
    state_dict = []
    for k, v in state_obj.items():
        state_dict.append(v)
    return render_template('7-states_list.html', state_dict=state_dict)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """
       display the states and cities listed in alphabetical order
    """
    state_obj = storage.all(State)
    state_dict = []
    for k, v in state_obj.items():
        state_dict.append(v)
    return render_template('8-cities_by_states.html', state_dict=state_dict)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
       a State object is found with this id
    """
    state_id = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown(exception):
    """
       remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
