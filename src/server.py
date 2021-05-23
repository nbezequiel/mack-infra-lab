from flask import Flask
from converter import ConverterService
import json
import socket

app = Flask(__name__)


@app.route("/convertemoeda/<value>")
def convert(value: float):
    converted = ConverterService().convert(value)
    response = app.response_class(
        response=json.dumps(converted.__dict__),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/")
def set_up():
    return "routing to %s" % socket.gethostname()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
