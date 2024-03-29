from db import db

class PPModel(db.Model):
    __tablename__ = "participant_physician"
    id = db.Column(db.Integer, primary_key=True)
    physician_name  = db.Column(db.String(55),nullable=False)
    physician_phone  = db.Column(db.String(55),  nullable=False)
    physician_address  = db.Column(db.String(155), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    participant = db.relationship('ParticipantModel', backref='participant_physician')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    user = db.relationship('UserModel', backref='participant_physician')
    
    def serialize(self):
        return {
            'id': self.id,
            'participant_id': self.participant_id,
            'physician_name':self.physician_name,
            'physician_phone': self.physician_phone,
            'physician_address' : self.physician_address,
            'created_by':self.created_by
            
            
        }