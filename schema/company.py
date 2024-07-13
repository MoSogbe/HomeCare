# schemas/company.py
from marshmallow import Schema, fields

class CompanySchema(Schema):
    id = fields.Int(dump_only=True)
    name_of_company = fields.Str(required=True)
    email = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    street_name = fields.Str(required=True)
    street_address = fields.Str(required=True)
    suite_unit = fields.Str(missing=None)  # Optional field
    city = fields.Str(required=True)
    state = fields.Str(required=True)
    logo_path = fields.Str(dump_only=True)  # This field is set during the POST request handling
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
