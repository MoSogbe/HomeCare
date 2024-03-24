from db import db

class ECIModel(db.Model):
    __tablename__ = "eci"
    id = db.Column(db.Integer, primary_key=True)
    gaurdian_name = db.Column(db.String(55), nullable=False)
    gaurdian_phone = db.Column(db.String(55), nullable=False)
    gaurdian_address = db.Column(db.String(225),  nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='eci')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    user = db.relationship('UserModel', backref='eci')
    
    def serialize(self):
        return {
            'id': self.id,
            'participant_id': self.participant_id,
            'gaurdian_name':self.gaurdian_name,
            'gaurdian_phone': self.gaurdian_phone,
            'gaurdian_address' : self.gaurdian_address,
            'created_by':self.created_by
            
            
        }