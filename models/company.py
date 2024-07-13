# models/company.py
from db import db
from datetime import datetime

class CompanyModel(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name_of_company = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(45), unique=True, nullable=False)
    street_name = db.Column(db.String(250), nullable=False)
    street_address = db.Column(db.String(250), nullable=False)
    suite_unit = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    logo_path = db.Column(db.String(255), nullable=True)  # New field for logo path
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    def __init__(self, name_of_company, email, phone_number, street_name, street_address, suite_unit, city, state, logo_path=None):
        self.name_of_company = name_of_company
        self.email = email
        self.phone_number = phone_number
        self.street_name = street_name
        self.street_address = street_address
        self.suite_unit = suite_unit
        self.city = city
        self.state = state
        self.logo_path = logo_path
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
