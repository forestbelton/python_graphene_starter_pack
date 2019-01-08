import json
from flask import Blueprint, request, Response
from werkzeug.exceptions import BadRequest

from .schema import schema

graphql_bp = Blueprint('graphql', __name__)

@graphql_bp.route('/', methods=['POST'])
def handle_graphql_request():
    data = request.get_json() or {}

    if 'query' in data and 'variables' in data:
        query = data['query']
        variables = data['variables']

        output = schema.execute(query, variables=variables)
        errors = output.errors or []
        result = {
            'data': output.data,
            'errors': [e.message for e in errors],
        }
    else:
        result = {
            'data': None,
            'errors': ['Malformed input query.'],
        }

    return Response(json.dumps(result), mimetype='application/json')
