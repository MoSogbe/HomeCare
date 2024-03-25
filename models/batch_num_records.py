from db import db

class BatchNumModel(db.Model):
    __tablename__ = "batch_num_records"
    id = db.Column(db.Integer, primary_key=True)
    batch_num = db.Column(db.String(125),  nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), nullable=False)
    drug = db.relationship('DrugModel', backref='batch_num_records')
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    
    
    def serialize(self):
        return {
            'id': self.id,
            'drug_id': self.drug_id,
            'batch_num': self.batch_num
        }