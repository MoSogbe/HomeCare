# models/administrative_documentation.py
from db import db
from datetime import datetime

class AdministrativeDocumentationModel(db.Model):
    __tablename__ = 'administrative_documentations'

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='administrative_documentations')
    document_type_id = db.Column(db.Integer, db.ForeignKey('document_types.id'), nullable=False)
    document_type = db.relationship('DocumentTypeModel', backref='administrative_documentations')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_by_user = db.relationship('UserModel', backref='administrative_documentations')
    file_path = db.Column(db.String(255), nullable=False)
    comment = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
