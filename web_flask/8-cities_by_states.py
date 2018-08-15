#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """display the states and cities listed in alphabetical order"""
    city_objs = storage.all(State)
    city_dict = []
    for k, v in city_objs.items():
        city_dict.append(v)
    return render_template('8-cities_by_states.html', city_dict=city_dict)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
