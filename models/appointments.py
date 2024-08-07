from datetime import datetime, timezone
from db import db

class AppointmentModel(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    doctor = db.Column(db.String(50), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    appointment_reason = db.Column(db.String(255), nullable=False)
    follow_up_date = db.Column(db.DateTime, nullable=True)
    follow_up_details = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    participant = db.relationship('ParticipantModel', backref='appointments')
    user = db.relationship('UserModel', backref='appointments')
