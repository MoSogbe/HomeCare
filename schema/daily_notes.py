from marshmallow import Schema, fields
from datetime import datetime

class DailyNoteSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    comment = fields.Str(required=True)
    reviewer_comment = fields.Str()  # New field for reviewer's comment
    participant_name = fields.String()
    created_by_username = fields.String()
    reviewed_by_username = fields.String()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class UpdateDailyNoteSchema(Schema):
    reviewer_comment = fields.Str(required=True)
    reviewed_by = fields.Int(required=True)

