from flask import Flask, jsonify
from checknum import check

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world"


@app.route("/check/<int:n>")
def check_num(n):
    response = {
        "Number": n,
        "Is": check(n),
        "IP": "192.168.1.1"
    }
    return jsonify(response)


@app.route("/add/<int:a>&<int:b>")
def add(a, b):
    result = a + b
    response = {
        "Numbers": [a, b],
        "Result": result,
        "IP": "192.168.1.1"
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
