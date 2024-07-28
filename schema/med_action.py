# schemas/med_action.py
from marshmallow import Schema, fields

class MedActionSchema(Schema):
    id = fields.Int(dump_only=True)
    mar_id = fields.Int(required=True)
    status_id = fields.Int(required=True)
    status = fields.Str(dump_only=True, attribute="status.status_name")
    administered_by = fields.Int(dump_only=True)
    caregiver_name = fields.Str(dump_only=True, attribute="user.fullname")
    participant_name = fields.Str(dump_only=True, attribute="mar.participant.name")
    created_at = fields.DateTime(dump_only=True)
