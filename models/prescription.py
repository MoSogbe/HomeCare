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
    comment = db.Column(db.String(225))
    drug = db.relationship('DrugModel', backref='prescriptions')
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='prescriptions')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('UserModel', backref='prescriptions')
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)