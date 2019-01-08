import json
from flask import Blueprint, request, Response
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import BadRequest

from python_graphene_starter_pack.schema import schema
from python_graphene_starter_pack.bp.request_schema import request_schema

graphql_bp = Blueprint('graphql', __name__)

@graphql_bp.route('/', methods=['POST'])
def handle_graphql_request():
    try:
        data = request_schema.load(request.get_json() or {})
        query = data['query']
        variables = data['variables']

        output = schema.execute(query, variables=variables)
        errors = output.errors or []
        result = {
            'data': output.data,
            'errors': [e.message for e in errors],
        }
    except ValidationError as e:
        result = {
            'data': None,
            'errors': e.messages,
        }

    return Response(json.dumps(result), mimetype='application/json')
