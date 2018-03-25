#!flask/bin/python
from flask import Blueprint
healthcheck_api = Blueprint('healthcheck_api', __name__, url_prefix='/api/v1.0')

@healthcheck_api.route("/healthcheck", methods=['GET'])
def healthcheck():
    return "Healthcheck: OK!"