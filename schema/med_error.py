# schemas/med_error.py
from marshmallow import Schema, fields

class MedErrorReasonSchema(Schema):
    id = fields.Int(dump_only=True)
    reason = fields.Str(required=True)

class MedErrorSchema(Schema):
    id = fields.Int(dump_only=True)
    drug_id = fields.Int(required=True)
    mar_id = fields.Int(required=True)
    participant_id = fields.Int(required=True)
    error_reason_id = fields.Int(required=True)
    error_reason = fields.Nested(MedErrorReasonSchema, dump_only=True)
    qty = fields.Int(required=True)
    comment = fields.Str(required=False)
    created_by = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
