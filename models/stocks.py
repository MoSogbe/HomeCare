from db import db

class StockModel(db.Model):
    __tablename__ = "stock"
    id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    transaction_code = db.Column(db.String(125))
    batch_code = db.Column(db.String(125), nullable=False)
    quantity_received = db.Column(db.String(12), nullable=False)
    expiry_date = db.Column(db.DateTime(), nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), nullable=False)
    drug = db.relationship('DrugModel', backref='stock')
    supplier = db.relationship('SupplierModel', backref='stock')
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)


    def serialize(self):
        return {
            'id': self.id,
            'supplier_id': self.supplier_id,
            'transaction_code': self.transaction_code,
            'batch_code':self.batch_code,
            'quantity_received':self.quantity_received,
            'expiry_date':self.expiry_date
        }