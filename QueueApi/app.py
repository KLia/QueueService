#!flask/bin/python
from flask import Flask, jsonify, Blueprint
from controllers.apis.healthcheck import healthcheck_api
from controllers.apis.queue import queue_api

app = Flask(__name__)
app.register_blueprint(healthcheck_api)
app.register_blueprint(queue_api)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0")