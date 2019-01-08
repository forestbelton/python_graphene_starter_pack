from flask import Flask
from python_graphene_starter_pack.bp.graphql_bp import graphql_bp

app = Flask(__name__)
app.register_blueprint(graphql_bp)
