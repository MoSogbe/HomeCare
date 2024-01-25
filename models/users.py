from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'), nullable=False)
    user_type = db.relationship('UserTypeModel', backref='users', lazy=True, overlaps="user_Types,users")
    
