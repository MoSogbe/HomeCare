from db import db

class VitalsModel(db.Model):
    __tablename__ = "vitals"
    id = db.Column(db.Integer, primary_key=True)
    blood_pressure = db.Column(db.String(24))
    systolic = db.Column(db.String(24))
    diastolic = db.Column(db.String(145))
    pulse = db.Column(db.String(24))
    glucose = db.Column(db.String(24))
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='vitals')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('UserModel', backref='vitals')
    comment = db.Column(db.String(225))
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)