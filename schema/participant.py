from db import db
from datetime import datetime

class ParticipantModel(db.Model):
    __tablename__ = 'participants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(120), nullable=False)
    ssn = db.Column(db.String(15), nullable=False)
    maid_number = db.Column(db.String(255), nullable=False)
    legal_status = db.Column(db.String(100))
    address_line_one = db.Column(db.String(255), nullable=False)
    address_line_two = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    home_phone = db.Column(db.String(100))
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'), nullable=False)
    gender = db.relationship('GenderModel', backref='participants', lazy=True, overlaps="gender,participants")
    bio_title_id = db.Column(db.Integer, db.ForeignKey('bio_titles.id'), nullable=False)
    bio_title = db.relationship('BTitleModel', backref='participants', lazy=True, overlaps="gender,participants")
    profile_image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
