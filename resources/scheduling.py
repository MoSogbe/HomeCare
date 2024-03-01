from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_
from models.scheduling import SchedulingModel
from schemas import SchedulingSchema
from datetime import datetime

blp = Blueprint("Scheduling", "scheduling", description="Operations on Scheduling & Assignmnets")

@blp.route("/scheduling/<string:scheduling_id>")
class ScheduleType(MethodView):
    @jwt_required()
    @blp.response(200, SchedulingSchema)
    def get(self, scheduling_id):
        scheduling = SchedulingModel.query.get_or_404(scheduling_id)
        return scheduling
    @jwt_required()
    def delete(self,scheduling_id):
        jwt = get_jwt()
        # if not jwt.get("is_admin"):
        #     abort(401, message="Admin privillege is required")
        try:
            scheduling = SchedulingModel.query.get_or_404(scheduling_id)
            db.session.delete(scheduling)
            db.session.commit()
            return {"message": "Schedule deleted."}
        except SQLAlchemyError as e:
                abort(500, message=f"An error occurred while deleting the Schedule. {e}")
    
   
    @jwt_required()
    @blp.arguments(SchedulingSchema)
    @blp.response(200, SchedulingSchema)
    def put(self, scheduling_data, scheduling_id):
        scheduling = SchedulingModel.query.get(scheduling_id)

        if scheduling:
            scheduling.name = scheduling_data["name"]
        else:
            scheduling = SchedulingModel(id=scheduling_id, **scheduling_data)

        db.session.add(scheduling)
        db.session.commit()

        return scheduling


@blp.route("/scheduling")
class SchedulingList(MethodView):
    @jwt_required()
    @blp.response(200, SchedulingSchema(many=True))
    def get(self):
        return SchedulingModel.query.all()
    @jwt_required()
    @blp.arguments(SchedulingSchema)
    @blp.response(201, SchedulingSchema)
    def post(self, scheduling_data):
        # Create a ParticipantModel instance
        scheduling = SchedulingModel(
            location_id=scheduling_data["location_id"],
            shift_period_id=scheduling_data["shift_period_id"],
            patient_id=scheduling_data["patient_id"],
            caregiver_id=scheduling_data["caregiver_id"],
            scheduled_by=scheduling_data["scheduled_by"],
            day_of_week=scheduling_data["day_of_week"],
            month=scheduling_data["month"],
            year=scheduling_data["year"],
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        try:
            db.session.add(scheduling)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the scheduling .{e}.")
        return scheduling
