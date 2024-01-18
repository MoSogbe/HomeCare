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
    id = fields.Int(dump_only=True)
    type_name = fields.Str(required=True)
    created_at = datetime.now()
    updated_at = datetime.now()
    
class UserTypeUpdateSchema(Schema):
    type_name = fields.Str(required=True)
    
    
class CompanySchema(Schema):
    id = fields.Int(dump_only=True)
    name_of_company = fields.Str(required=True)
    email = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    address = fields.Str(required=True)
    created_at = datetime.now()
    updated_at = datetime.now()
    
class ServiceCategorySchema(Schema):
    id = fields.Int(dump_only=True)
    category_name = fields.Str(required=True)
    created_at = datetime.now()
    updated_at = datetime.now()
    
class ServiceCategoryUpdateSchema(ServiceCategorySchema):
    category_name = fields.Str(required=True)
    
class ServiceSchema(Schema):
    id = fields.Int(dump_only=True)
    service_name = fields.Str(required=True)
    service_price = fields.Str(required=True)
    service_charge_duration = fields.Str(required=True)
    service_charge_frequency = fields.Str(required=True)
    service_category = fields.Str(required=True)
    created_at = datetime.now()
    updated_at = datetime.now()
    
class ServiceUpdateSchema(Schema):
    service_name = fields.Str(required=True)
    service_price = fields.Str(required=True)
    service_charge_duration = fields.Str(required=True)
    service_charge_frequency = fields.Str(required=True)
    service_category = fields.Str(required=True)
    
class UoMSchema(Schema):
    id = fields.Int(dump_only=True)
    unit_name = fields.Str(required=True)
    symbol = fields.Str(required=True)
    
    
    