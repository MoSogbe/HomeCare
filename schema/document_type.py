from marshmallow import Schema, fields

class DocumentTypeSchema(Schema):
    id = fields.Int(dump_only=True)
    document_type = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
