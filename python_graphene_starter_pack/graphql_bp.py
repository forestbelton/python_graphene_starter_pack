from flask import Blueprint, request

graphql_bp = Blueprint('graphql', __name__)

@graphql_bp.route('/')
def handle_graphql_request():
    return 'OK'
