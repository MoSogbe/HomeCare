from db import db

class ParticipantDocumentationModel(db.Model):
    __tablename__ = "participant_documentations"

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    document_type_id = db.Column(db.Integer, db.ForeignKey('document_types.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    participant = db.relationship('ParticipantModel', backref='participant_documentations')
    document_type = db.relationship('DocumentTypeModel', backref='participant_documentations')
    user = db.relationship('UserModel', backref='participant_documentations')

    def serialize(self):
        return {
            'id': self.id,
            'participant_id': self.participant_id,
            'document_type_id': self.document_type_id,
            'document_type': self.document_type.document_type,  # Add this line
            'file_path': self.file_path,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
