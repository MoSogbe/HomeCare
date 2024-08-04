from db import db

class MedErrorReasonModel(db.Model):
    __tablename__ = "med_error_reasons"

    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.String(80), nullable=False)

    med_errors = db.relationship("MedErrorModel", back_populates="error_reason")
