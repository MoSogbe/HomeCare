from db import db

class UoMModel(db.Model):
    __tablename__ = "unit_of_measurements"

    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String(45), unique=True, nullable=False)
    symbol = db.Column(db.String(11), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    
