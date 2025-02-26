"""This file will create the server and accept the backend processes."""

from asyncio import run
from flask import Flask

from dataio import test_data


app: Flask = Flask(__name__)


@app.route("/")
async def hello_world():
    """Debug Def."""
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    print("Running main.py")
    run(test_data())
    """
    try:
        print("Setting Up the Server...")
        app.run()
    except Exception as e:
        print("There was a problem setting up the server here is the error info:")
        print(e)
        exit(-1)
    """
