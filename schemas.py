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
    username = fields.Str(required=True)
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

class SchedulingReport(Schema):
    id = fields.Int(dump_only=True)
    start_date = fields.Str(required=True)
    end_date = fields.Str(required=True)
    report_type = fields.Str(required=True)

class ParticipantServiceProviderHistorySchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Str(required=True)
    service_type_id = fields.Int(required=True)
    provider_name = fields.Str(required=True)
    provider_address = fields.Str(required=True)
    provider_phone = fields.Str(required=True)

class DiagnosisSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    axis_id = fields.Int(required=True)
    medical_condition_id = fields.Int(required=True)

class DiagnosisViewSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    medical_condition_id = fields.Int(required=True)
    condition_name = fields.Str(required=True)
    axis_name = fields.Str(required=True)
    created_by = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class MITSchema(Schema):
    id = fields.Int(dump_only=True)
    mit_name = fields.Str(required=True)

class MISchema(Schema):
    id = fields.Int(dump_only=True)
    mit_id = fields.Int(required=True)
    participant_id = fields.Int(required=True)
    created_by = fields.Int(required=True)
    medical_condition_id = fields.Int(required=True)

class MIViewSchema(Schema):
    id = fields.Int(dump_only=True)
    mit_id = fields.Int(required=True)
    participant_id = fields.Int(required=True)
    created_by = fields.Int(required=True)
    medical_condition_id = fields.Int(required=True)
    condition_name = fields.String(required=True)

class ECISchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    created_by = fields.Int(required=True)
    gaurdian_name = fields.Str(required=True)
    gaurdian_phone = fields.Str(required=True)
    gaurdian_address = fields.Str(required=True)


class CaseManagerSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    created_by = fields.Int(required=True)
    cm_name = fields.Str(required=True)
    cm_phone = fields.Str(required=True)
    cm_emergency_phone = fields.Str(required=True)
    cm_address = fields.Str(required=True)
    cm_fax = fields.Str(required=True)
    cm_email_address = fields.Str(required=True)

class PreferredHospitalSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    created_by = fields.Int(required=True)
    ph_name = fields.Str(required=True)
    ph_address = fields.Str(required=True)

class ParticipantsPhysicianSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    created_by = fields.Int(required=True)
    physician_name = fields.Str(required=True)
    physician_phone = fields.Str(required=True)
    physician_address = fields.Str(required=True)

class DrugCategorySchema(Schema):
    id = fields.Int(dump_only=True)
    drug_category_name = fields.Str(required=True)

class DrugSchema(Schema):
    id = fields.Int(dump_only=True)
    drug_category_id = fields.Str(required=True)
    brand_name = fields.Str(required=True)
    drug_name = fields.Str(required=True)
    generic_name = fields.Str(required=True)
    uom_id = fields.Str(required=True)

class SupplierSchema(Schema):
    id = fields.Int(dump_only=True)
    supplier_name = fields.Str(required=True)
    supplier_phone = fields.Str(required=True)
    supplier_address = fields.Str(required=True)
    supplier_contact_person = fields.Str(required=True)
    supplier_balance = fields.Str(required=True)

class StockSchema(Schema):
    id = fields.Int(dump_only=True)
    transaction_code = fields.Str(required=True)
    batch_code = fields.Str(required=True)
    supplier_id = fields.Str(required=True)
    drug_id = fields.Str(required=True)
    quantity_received = fields.Str(required=True)
    expiry_date = fields.Str(required=True)

class StockListSchema(Schema):
    id = fields.Int(dump_only=True)
    transaction_code = fields.Str(required=True)
    batch_code = fields.Str(required=True)
    supplier_id = fields.Str(required=True)
    drug_id = fields.Str(required=True)
    drug_name = fields.Str(required=True)
    quantity_received = fields.Str(required=True)
    expiry_date = fields.Str(required=True)

class StockTotalSchema(Schema):
    id = fields.Int(dump_only=True)
    total_qty = fields.Str(required=True)
    drug_id = fields.Str(required=True)

class BatchNumSchema(Schema):
    id = fields.Int(dump_only=True)
    batch_num = fields.Str(required=True)
    drug_id = fields.Str(required=True)

class ReportRequestSchema(Schema):
    category_id = fields.Integer()
    product_id = fields.Integer()

class ReportResponseSchema(Schema):
    category_id = fields.Integer()
    category_name = fields.String()
    product_id = fields.Integer()
    product_name = fields.String()
    total_stock = fields.Integer()

class InvoiceSpecificRequestSchema(Schema):
    transaction_code = fields.String()

class InvoiceSpecificResponseSchema(Schema):
    transaction_code = fields.String()
    batch_code = fields.String()
    quantity_received = fields.String()
    expiry_date = fields.DateTime()
    drug_name = fields.String()
    supplier_name = fields.String()
    supplier_phone = fields.String()
    supplier_address = fields.String()
    supplier_contact_person = fields.String()

class PrescriptionSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    drug_id = fields.Int(required=True)
    reason_for_medication = fields.Str(required=True)
    mar_date = fields.Str(required=True)
    mar_time = fields.Str(required=True)
    date_from = fields.Str(required=True)
    date_to = fields.Str(required=True)
    place_of_mar = fields.Str(required=True)
    dossage = fields.Str(required=True)
    frequency = fields.Int(required=True)
    qty = fields.Int(required=True)
    comment = fields.Str(required=True)


class PrescriptionUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    drug_id = fields.Int(required=True)
    reason_for_medication = fields.Str(required=True)
    mar_date = fields.Str(required=True)
    mar_time = fields.Str(required=True)
    date_from = fields.Str(required=True)
    date_to = fields.Str(required=True)
    place_of_mar = fields.Str(required=True)
    dossage = fields.Str(required=False)
    frequency = fields.Int(required=True)
    qty = fields.Int(required=True)
    comment = fields.Str(required=True)
    #created_by = fields.Int(required=True)

class PrescriptionQuerySchema(Schema):
    date_from = fields.DateTime(required=True)
    date_to = fields.DateTime(required=True)




