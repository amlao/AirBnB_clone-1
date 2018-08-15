#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State
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


@app.teardown_appcontext
def teardown(exception):
    """
       remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
