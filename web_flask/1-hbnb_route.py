#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """
       a script that starts a Flask web application
    """
    return "Hello HBNB!"

@app.route('/', strict_slashes=False)
def hbnb():
    """
       a script that starts a Flask web application
    """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
