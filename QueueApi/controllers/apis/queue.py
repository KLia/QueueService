#!flask/bin/python
from flask import request, Blueprint, jsonify, abort, make_response
import json
from controllers.queue import Queue
from models.queue.queue_item import QueueItem

queue_api = Blueprint('queue_api', __name__, url_prefix='/api/v1.0')

#Create a Queue on startup
queue = Queue()
error_msg = {'message': 'There was an error processing your request'}

#Handles 400 error messages
@queue_api.errorhandler(400)
def custom400(error):
    return make_response(jsonify({'message': error.description}), 404)

#Pushes an item into the queue
#Requires a JSON request with 'File' and 'Text' 
@queue_api.route("/queue/items/enqueue", methods=['POST'])
def queue_item(): 
    try:
        if not request.json or not 'file' in request.json or not 'text' in request.json:
            abort(400, 'Please provide both \'file\' and \'text\' in json message body')
        
        item = QueueItem(request.json['file'], request.json['text'])
        item_json = item.to_json()
        queue.enqueue(item_json)

        return_data = {
            'message': 'Processed OK',
            'queue_size': queue.size(),
            'item': item_json
        }

        return jsonify(return_data)
    except:
        return make_response(jsonify(error_msg), 500)

@queue_api.route("/queue/items/dequeue", methods=['GET'])
def get_item():
    try:
        return_data = {
            'message': 'Processed OK',
            'item': queue.dequeue(),
            'queue_size': queue.size()
        }

        return jsonify(return_data)
    except:
        return make_response(jsonify(error_msg), 500)