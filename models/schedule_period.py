from db import db

class SchedulePeriodModel(db.Model):
    __tablename__ = "schedule_periods"

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.String(12), unique=False, nullable=False)
    end_time = db.Column(db.String(12), unique=False, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)