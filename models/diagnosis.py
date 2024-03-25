from db import db

class DiagnosisModel(db.Model):
    __tablename__ = "diagnosis"
    id = db.Column(db.Integer, primary_key=True)
    medical_condition_id = db.Column(db.Integer, db.ForeignKey('medical_conditions.id'), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='diagnosis')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('UserModel', backref='diagnosis')
    medical_condition = db.relationship('MedicalConditionModel', backref='diagnosis')
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'participant_id': self.participant_id,
            'medical_condition_id':self.medical_condition_id,
            'created_by':self.created_by
            
            
        }