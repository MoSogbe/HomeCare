from db import db

class BTitleModel(db.Model):
    __tablename__ = "bio_titles"

    id = db.Column(db.Integer, primary_key=True)
    bio_name = db.Column(db.String(12), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)