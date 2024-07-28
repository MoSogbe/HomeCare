# schemas/med_action_status.py
from marshmallow import Schema, fields

class MedActionStatusSchema(Schema):
    id = fields.Int(dump_only=True)
    status_name = fields.Str(required=True)
    description = fields.Str()
