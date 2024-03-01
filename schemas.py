from marshmallow import Schema, fields
from datetime import datetime
 

class UserTypeSchema(Schema):
    id = fields.Int(dump_only=True)
    type_name = fields.Str(required=True)
    created_at = datetime.now()
    updated_at = datetime.now()
    
class UserTypeUpdateSchema(Schema):
    type_name = fields.Str(required=True)
    
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    
class FetchUserSchema(Schema):
    id = fields.Int(dump_only=True)
    fullname = fields.Str(required=True)
    user_type = fields.Nested(UserTypeSchema)
    username = fields.Str(required=True)

class UserListSchema(Schema):
    users = fields.Nested(FetchUserSchema, many=True)
    
class UserRegistersSchema(UserSchema):
    fullname = fields.Str(required=True)
    email = fields.Str(required=True)
    user_type = fields.Str(required=True)
    
    
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
    
class BStatusSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Str(required=True)
    
class MedicalConditionSchema(Schema):
    id = fields.Int(dump_only=True)
    condition_name = fields.Str(required=True)
    
class GenderSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    
class BioTitleSchema(Schema):
    id = fields.Int(dump_only=True)
    bio_name = fields.Str(required=True)
    
    
class StaffSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    address = fields.Str(required=True)
    location = fields.Str(required=True)
    gender_id = fields.Str(required=True)
    bio_title_id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    profile_image = fields.Str(required=True)
    
class ParticipantSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    dob = fields.Str(required=True)
    ssn = fields.Str(required=True)
    maid_number = fields.Str(required=True)
    legal_status = fields.Str(required=True)
    home_address = fields.Str(required=True)
    home_phone = fields.Str(required=True)
    gender_id = fields.Str(required=True)
    bio_title_id = fields.Str(required=True)
    profile_image = fields.Str(required=True)
         
class LocationSchema(Schema):
    id = fields.Int(dump_only=True)
    location_name = fields.Str(required=True)
    
class LocationUpdateSchema(Schema):
    location_name = fields.Str(required=True)
    
class SchedulePeriodSchema(Schema):
    id = fields.Int(dump_only=True)
    start_time = fields.Str(required=True)
    end_time = fields.Str(required=True)
    
class SchedulePeriodUpdateSchema(Schema):
    start_time = fields.Str(required=True)
    end_time = fields.Str(required=True)
    
class SchedulingSchema(Schema):
    id = fields.Int(dump_only=True)
    location_id = fields.Str(required=True)
    shift_period_id = fields.Str(required=True)
    patient_id = fields.Str(required=True)
    caregiver_id = fields.Str(required=True)
    scheduled_by = fields.Str(required=True)
    day_of_week = fields.Str(required=True)
    month = fields.Str(required=True)
    year = fields.Str(required=True)
    
    
   
    
    
    