from marshmallow import Schema, fields
from datetime import datetime
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
   
    
class UserRegistersSchema(UserSchema):
    fullname = fields.Str(required=True)
    email = fields.Str(required=True)
    user_type = fields.Str(required=True)
    
class UserTypeSchema(Schema):
    type_name = fields.Str(required=True)
    created_at = datetime.now()
    updated_at = datetime.now()
    
    