from db import db

class UserTypeModel(db.Model):
    __tablename__ = "user_types"

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    user = db.relationship('UserModel', backref='user_types', overlaps="users,user_type")
    
