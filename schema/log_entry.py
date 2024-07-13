from marshmallow import Schema, fields
from datetime import datetime

class LogEntrySchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    check_in = fields.DateTime(required=True)
    check_out = fields.DateTime(required=False)
    notes = fields.Str()
    service_id = fields.Int()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
