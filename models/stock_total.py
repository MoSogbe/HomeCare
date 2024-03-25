from db import db

class StockTotalModel(db.Model):
    __tablename__ = "stock_total"
    id = db.Column(db.Integer, primary_key=True)
    total_qty = db.Column(db.String(125),  nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), nullable=False)
    drug = db.relationship('DrugModel', backref='stock_total')
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    
    
    def serialize(self):
        return {
            'id': self.id,
            'drug_id': self.drug_id,
            'total_qty': self.total_qty
        }