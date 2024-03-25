from db import db

class SupplierModel(db.Model):
    __tablename__ = "supplier"

    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(12), unique=True, nullable=False)
    supplier_phone = db.Column(db.String(12), unique=True)
    supplier_address = db.Column(db.String(155))
    supplier_contact_person = db.Column(db.String(120))
    supplier_balance = db.Column(db.String(12),default=0)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)