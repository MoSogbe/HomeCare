from datetime import datetime
from models.base_model import BaseModel
from db import db


class MedErrorModel(BaseModel):
    __tablename__ = "med_errors"

    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), nullable=False)
    mar_id = db.Column(db.Integer, db.ForeignKey('prescriptions.id'), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    error_reason_id = db.Column(db.Integer, db.ForeignKey('med_error_reasons.id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(225))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    prescription = db.relationship("PrescriptionModel", back_populates="med_errors")
    drug = db.relationship("DrugModel")
    participant = db.relationship("ParticipantModel")
    error_reason = db.relationship("MedErrorReasonModel")
    user = db.relationship('UserModel')
