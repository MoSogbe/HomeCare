from db import db

class DrugCategoryModel(db.Model):
    __tablename__ = "drug_category"

    id = db.Column(db.Integer, primary_key=True)
    drug_category_name = db.Column(db.String(45), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)