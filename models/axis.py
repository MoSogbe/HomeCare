# models/axis.py
from db import db
from datetime import datetime

class AxisModel(db.Model):
    __tablename__ = "axis"

    id = db.Column(db.Integer, primary_key=True)
    axis_type = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
