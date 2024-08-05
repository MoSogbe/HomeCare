from db import db
from datetime import datetime

class MedActionModel(db.Model):
    __tablename__ = "med_actions"

    id = db.Column(db.Integer, primary_key=True)
    mar_id = db.Column(db.Integer, db.ForeignKey("prescriptions.id"), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey("med_action_statuses.id"), nullable=False)
    administered_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    prescription = db.relationship("PrescriptionModel", back_populates="med_actions")
    user = db.relationship("UserModel", back_populates="med_actions")
    status = db.relationship("MedActionStatusModel", back_populates="med_actions")
