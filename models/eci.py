from db import db

class ECIModel(db.Model):
    __tablename__ = "eci"
    id = db.Column(db.Integer, primary_key=True)
    gaurdian_name = db.Column(db.String(55), unique=True, nullable=False)
    gaurdian_phone = db.Column(db.String(55), unique=True, nullable=False)
    gaurdian_address = db.Column(db.String(225), unique=True, nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='mit')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    user = db.relationship('UserModel', backref='medical_information')