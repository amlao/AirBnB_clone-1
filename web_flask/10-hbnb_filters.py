#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
       State, City and Amenity objects must be loaded from DBStorage
    """
    return render_template('10-hbnb_filters',
                           states=storage.all('State'),
                           amenities=storage.all('Amenity'))


@app.teardown_appcontext
def teardown(exception):
    """
       remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
