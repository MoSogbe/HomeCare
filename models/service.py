from db import db

class ServiceModel(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    service_category = db.Column(db.Integer, db.ForeignKey('service_categories.id'), nullable=False)
    service_name = db.Column(db.String(120), unique=True, nullable=False)
    service_price = db.Column(db.String(80), unique=True, nullable=False)
    service_charge_duration = db.Column(db.String(45), unique=True, nullable=False)
    service_charge_frequency = db.Column(db.String(45), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    
