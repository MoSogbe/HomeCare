from db import db

class CareGiverModel(db.Model):
    __tablename__ = 'caregivers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(100))
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'), nullable=False)
    gender = db.relationship('GenderModel', backref='caregivers', lazy=True,overlaps="gender,caregivers")
    bio_title_id = db.Column(db.Integer, db.ForeignKey('bio_titles.id'), nullable=False)
    bio_title = db.relationship('BTitleModel', backref='caregivers', lazy=True,overlaps="gender,caregivers")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('UserModel', backref='caregivers', lazy=True,overlaps="gender,caregivers")
    profile_image = db.Column(db.String(255), nullable=True) 
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
