# schemas/axis.py
from marshmallow import Schema, fields

class GiveSchema(Schema):
    id = fields.Int(dump_only=True)
    status_id = fields.Int(required=True)

