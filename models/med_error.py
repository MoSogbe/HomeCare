from db import db
from datetime import datetime

class MedErrorModel(db.Model):
    __tablename__ = "med_errors"
    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), nullable=False)
    mar_id = db.Column(db.Integer, db.ForeignKey('prescriptions.id'), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    error_reason_id = db.Column(db.Integer, db.ForeignKey('med_error_reasons.id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(225))
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    prescription = db.relationship("PrescriptionModel", back_populates="med_errors")
    drug = db.relationship("DrugModel")
    participant = db.relationship("ParticipantModel")
    error_reason = db.relationship("MedErrorReasonModel")
