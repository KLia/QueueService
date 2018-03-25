#!flask/bin/python
from flask import Flask, jsonify, Blueprint
from apis.healthcheck import healthcheck_api
from apis.queue import queue_api

app = Flask(__name__)
app.register_blueprint(healthcheck_api)
app.register_blueprint(queue_api)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': '3'})

if __name__ == '__main__':
    app.run(host="0.0.0.0")