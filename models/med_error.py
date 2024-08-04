# models/med_error.py
from db import db
from datetime import datetime

class MedErrorModel(db.Model):
    __tablename__ = "med_errors"

    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, nullable=False)
    mar_id = db.Column(db.Integer, nullable=False)
    participant_id = db.Column(db.Integer, nullable=False)
    error_reason_id = db.Column(db.Integer, db.ForeignKey('med_error_reasons.id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    error_reason = db.relationship("MedErrorReasonModel", back_populates="med_errors")
