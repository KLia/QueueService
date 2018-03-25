#!flask/bin/python
from flask import request, Blueprint, jsonify, abort
import json
from controllers.queue import Queue

queue_api = Blueprint('queue_api', __name__, url_prefix='/api/v1.0')

#Create a Queue on startup
queue = Queue()

@queue_api.route("/queue/items/enqueue", methods=['POST'])
def queue_item(): 
    if not request.json or not 'file' in request.json or not 'text' in request.json:
        abort(400)
        
    queue.enqueue(request.json)
    return_data = {
        'message': 'Processed OK',
        'queue_size': queue.size()
    }

    return jsonify(return_data)

@queue_api.route("/queue/items/dequeue", methods=['GET'])
def get_item():
    return_data = {
        'message': 'Processed OK'
        'item': queue.dequeue(),
        'queue_size': queue.size()
    }

    return jsonify(return_data)