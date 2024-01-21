from db import db

class BStatusModel(db.Model):
    __tablename__ = "behavioral_statuses"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(12), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    
