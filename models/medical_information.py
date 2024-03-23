from db import db

class MedicalInformationModel(db.Model):
    __tablename__ = "medical_information"
    id = db.Column(db.Integer, primary_key=True)
    mi_name = db.Column(db.String(25), unique=True, nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='mit')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    user = db.relationship('UserModel', backref='medical_information')