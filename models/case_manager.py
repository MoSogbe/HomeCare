from db import db

class CaseManagerModel(db.Model):
    __tablename__ = "case_manager"
    id = db.Column(db.Integer, primary_key=True)
    cm_name = db.Column(db.String(55), nullable=False)
    cm_phone = db.Column(db.String(55), nullable=False)
    cm_emergency_phone = db.Column(db.String(55))
    cm_address = db.Column(db.String(225),  nullable=False)
    cm_fax = db.Column(db.String(45),  nullable=True)
    cm_email_address = db.Column(db.String(125))
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='case_manager')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    user = db.relationship('UserModel', backref='case_manager')
    
    def serialize(self):
        return {
            'id': self.id,
            'participant_id': self.participant_id,
            'cm_name':self.cm_name,
            'cm_phone': self.cm_phone,
            'cm_fax': self.cm_fax,
            'cm_emergency_phone' : self.cm_emergency_phone,
            'cm_address': self.cm_address,
            'cm_email_address': self.cm_email_address,
            'created_by':self.created_by
            
            
        }