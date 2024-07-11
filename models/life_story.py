from db import db
from datetime import datetime

class LifeStoryModel(db.Model):
    __tablename__ = "life_stories"

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    participant = db.relationship('ParticipantModel', backref='life_stories')
    creator = db.relationship('UserModel', backref='life_stories')
