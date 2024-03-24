from db import db

class CaseManagerModel(db.Model):
    __tablename__ = "case_manager"
    id = db.Column(db.Integer, primary_key=True)
    cm_name = db.Column(db.String(55), unique=True, nullable=False)
    cm_phone = db.Column(db.String(55), unique=True, nullable=False)
    cm_emergency_phone = db.Column(db.String(55), unique=True)
    cm_address = db.Column(db.String(225), unique=True, nullable=False)
    cm_fax = db.Column(db.String(45), unique=True)
    cm_email_address = db.Column(db.String(125), unique=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='case_manager')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    user = db.relationship('UserModel', backref='case_manager')