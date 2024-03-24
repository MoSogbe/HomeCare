from db import db

class MITModel(db.Model):
    __tablename__ = "mit"
    id = db.Column(db.Integer, primary_key=True)
    mit_name = db.Column(db.String(25),  nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)