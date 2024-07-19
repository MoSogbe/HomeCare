from db import db
from datetime import datetime

class DocumentTypeModel(db.Model):
    __tablename__ = 'document_types'

    id = db.Column(db.Integer, primary_key=True)
    document_type = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
