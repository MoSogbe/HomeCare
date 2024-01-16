from db import db

class ServiceCategoryModel(db.Model):
    __tablename__ = "service_categories"

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(45), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    service = db.relationship('ServiceModel', backref='service_categories', lazy=True)
    
