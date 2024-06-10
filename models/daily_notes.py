from db import db

class DailyNotesModel(db.Model):
    __tablename__ = "daily_notes"

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='daily_notes')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('UserModel', backref='daily_notes')
    reviewed_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.Column(db.String(425),nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)


