from marshmallow import Schema, fields
from datetime import datetime

class DailyNoteSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    comment = fields.Str(required=True)
    reviewed_by = fields.Int()

