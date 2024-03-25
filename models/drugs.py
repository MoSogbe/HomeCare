from db import db

class DrugModel(db.Model):
    __tablename__ = "drugs"
    id = db.Column(db.Integer, primary_key=True)
    drug_category_id = db.Column(db.Integer, db.ForeignKey('drug_category.id'), nullable=False)
    drug_name = db.Column(db.String(125), unique=True, nullable=False)
    generic_name = db.Column(db.String(125), nullable=False)
    brand_name = db.Column(db.String(125), nullable=False)
    uom_id = db.Column(db.Integer, db.ForeignKey('unit_of_measurements.id'), nullable=False)
    uom = db.relationship('UoMModel', backref='drugs')
    drug_category = db.relationship('DrugCategoryModel', backref='drugs')
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    
    
    def serialize(self):
        return {
            'id': self.id,
            'drug_category_id': self.drug_category_id,
            'uom_id': self.uom_id,
            'drug_name':self.drug_name,
            'brand_name':self.brand_name,
            'generic_name':self.generic_name
        }