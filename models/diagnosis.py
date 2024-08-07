# models/diagnosis.py
from db import db
from datetime import datetime

class DiagnosisModel(db.Model):
    __tablename__ = "diagnosis"
    id = db.Column(db.Integer, primary_key=True)
    medical_condition_id = db.Column(db.Integer, db.ForeignKey('medical_conditions.id'), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    axis_id = db.Column(db.Integer, db.ForeignKey('axis.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    participant = db.relationship('ParticipantModel', backref='diagnosis')
    user = db.relationship('UserModel', backref='diagnosis')
    medical_condition = db.relationship('MedicalConditionModel', backref='diagnosis')
    axis = db.relationship('AxisModel', backref='diagnosis')

    def serialize(self):
        return {
            'id': self.id,
            'participant_id': self.participant_id,
            'medical_condition_id': self.medical_condition_id,
            'axis_id': self.axis_id,
            'created_by': self.created_by,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
