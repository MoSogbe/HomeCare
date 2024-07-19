from db import db
from datetime import datetime

class ParticipantDocumentationModel(db.Model):
    __tablename__ = "participant_documentations"

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    document_type_id = db.Column(db.Integer, db.ForeignKey('document_types.id'), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    participant = db.relationship('ParticipantModel', backref='participant_documentations')
    user = db.relationship('UserModel', backref='participant_documentations')
    document_type = db.relationship('DocumentTypeModel', backref='participant_documentations')
