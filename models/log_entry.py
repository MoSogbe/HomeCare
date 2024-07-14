from db import db
class LogEntryModel(db.Model):
    __tablename__ = "log_entries"

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='log_entries')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('UserModel', backref='log_entries')
    check_in = db.Column(db.DateTime, nullable=False, default=db.func.now())
    check_out = db.Column(db.DateTime, nullable=True)
    notes = db.Column(db.String(255))
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    service = db.relationship('ServiceModel', backref='log_entries')
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, default=db.func.now())
