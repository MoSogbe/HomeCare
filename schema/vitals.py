from marshmallow import Schema, fields
from datetime import datetime

class VitalsSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    blood_pressure = fields.Int(required=True)
    systolic = fields.Str(required=True)
    diastolic = fields.Str(required=True)
    pulse = fields.Str(required=True)
    glucose = fields.Str(required=True)
    comment = fields.Str(required=True)
