from db import db

class MedicalConditionModel(db.Model):
    __tablename__ = "medical_conditions"

    id = db.Column(db.Integer, primary_key=True)
    condition_name = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    
