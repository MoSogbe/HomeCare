from marshmallow import Schema, fields


class BehavioralIssuesSchema(Schema):
    details = fields.String(required=True)


class BehavioralIssuesResponseSchema(Schema):
    id = fields.Integer(required=True)
    details = fields.String(required=True)
    participant_id = fields.Integer(required=True)
    created_by = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
