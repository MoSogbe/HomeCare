from datetime import datetime
from db import db


class PrescriptionModel(db.Model):
    __tablename__ = "prescriptions"

    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), nullable=False)
    reason_for_medication = db.Column(db.String(145), nullable=False)
    mar_date = db.Column(db.String(24), nullable=False)
    mar_time = db.Column(db.String(24), nullable=False)
    date_from = db.Column(db.String(24), nullable=False)
    date_to = db.Column(db.String(24), nullable=False)
    place_of_mar = db.Column(db.String(125))
    dossage = db.Column(db.String(125), nullable=False)
    frequency = db.Column(db.Integer, nullable=True)
    qty = db.Column(db.Integer, nullable=True)
    todays_frequency = db.Column(db.Integer, nullable=False, default=0)
    comment = db.Column(db.String(225))
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    drug = db.relationship('DrugModel', backref='prescriptions')
    participant = db.relationship('ParticipantModel', backref='prescriptions')
    user = db.relationship('UserModel', backref='prescriptions')
    administrations = db.relationship("AdministrationModel", back_populates="prescription", cascade="all, delete-orphan", overlaps="prescription")
    med_errors = db.relationship("MedErrorModel", back_populates="prescription", cascade="all, delete-orphan")
    med_actions = db.relationship("MedActionModel", back_populates="prescription", cascade="all, delete-orphan")
