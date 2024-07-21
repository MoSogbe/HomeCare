from marshmallow import Schema, fields

class ParticipantDocumentationSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    document_type_id = fields.Int(required=True)
    document_type = fields.Str(dump_only=True)
    created_by = fields.Int(dump_only=True)
    file_path = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
