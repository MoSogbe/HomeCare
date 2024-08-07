from datetime import datetime

from db import db


class AdministrationModel(db.Model):
    __tablename__ = "administrations"

    id = db.Column(db.Integer, primary_key=True)
    mar_id = db.Column(db.Integer, db.ForeignKey('prescriptions.id'), nullable=False)
    administered_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    administered_by = db.Column(db.String(50), nullable=False)

    prescription = db.relationship("PrescriptionModel", back_populates="administrations", overlaps="prescriptions")
