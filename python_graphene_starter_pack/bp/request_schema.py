from marshmallow import Schema, fields

class RequestSchema(Schema):
    query = fields.Str(required=True)
    variables = fields.Dict(allow_none=True, missing={})

request_schema = RequestSchema(strict=True)
