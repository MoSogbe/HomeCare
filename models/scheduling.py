from db import db

class SchedulingModel(db.Model):
    __tablename__ = "scheduling"
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    shift_period_id = db.Column(db.Integer, db.ForeignKey('schedule_periods.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('participants.id'), nullable=False)
    caregiver_id = db.Column(db.Integer, db.ForeignKey('caregivers.id'), nullable=False)
    day_of_week = db.Column(db.String(10), nullable=False)  # Store day of the week as a string
    month = db.Column(db.Integer, nullable=False)  # Add a column for month
    year = db.Column(db.Integer, nullable=False)   # Add a column for year
    scheduled_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    location = db.relationship('LocationModel', backref='scheduling')
    shift_period = db.relationship('SchedulePeriodModel', backref='scheduling')
    patient = db.relationship('ParticipantModel', backref='scheduling')
    caregiver = db.relationship('CareGiverModel', backref='scheduling')
    created_by = db.relationship('UserModel', backref='scheduling')
    