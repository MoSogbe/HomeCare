from db import db

class PHModel(db.Model):
    __tablename__ = "preferred_hospital"
    id = db.Column(db.Integer, primary_key=True)
    ph_name = db.Column(db.String(55), unique=True, nullable=False)
    ph_address = db.Column(db.String(155), unique=True, nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='preferred_hospital')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    user = db.relationship('UserModel', backref='preferred_hospital')