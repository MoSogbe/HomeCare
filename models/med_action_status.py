# models/med_action_status.py
from db import db

class MedActionStatusModel(db.Model):
    __tablename__ = "med_action_statuses"

    id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))
    med_actions = db.relationship("MedActionModel", back_populates="status")
