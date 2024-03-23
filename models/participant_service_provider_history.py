from db import db

class ParticipantServiceProviderHistoryModel(db.Model):
    __tablename__ = "participant_service_provider_history"

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='participant_service_provider_history')
    service_type_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    provider_name = db.Column(db.String(55), unique=True, nullable=False)
    provider_address = db.Column(db.String(155), unique=True, nullable=False)
    provider_phone = db.Column(db.String(155), unique=True, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    service_type = db.relationship('ServiceModel', backref='participant_service_provider_history')
    user = db.relationship('UserModel', backref='participant_service_provider_history')