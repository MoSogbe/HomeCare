from flask import request
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.appointments import AppointmentModel
from schema.appointments import AppointmentSchema

blp = Blueprint("Appointments", "appointments", description="Operations on Appointments")


@blp.route("/appointments")
class AppointmentsList(MethodView):
    @jwt_required()
    @blp.response(200, AppointmentSchema(many=True))
    def get(self):
        search = request.args.get('search', '')

        query = AppointmentModel.query

        if search:
            search = f"%{search}%"
            query = query.filter(
                db.or_(
                    AppointmentModel.doctor.ilike(search),
                    AppointmentModel.appointment_reason.ilike(search)
                )
            )

        appointments = query.all()
        return appointments

    @jwt_required()
    @blp.arguments(AppointmentSchema)
    @blp.response(201, AppointmentSchema)
    def post(self, appointment_data):
        appointment = AppointmentModel(**appointment_data, created_by=get_jwt_identity())
        try:
            db.session.add(appointment)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while creating the appointment. {e}")
        return appointment


@blp.route("/appointment/<string:appointment_id>")
class AppointmentResource(MethodView):
    @jwt_required()
    @blp.response(200, AppointmentSchema)
    def get(self, appointment_id):
        appointment = AppointmentModel.query.get_or_404(appointment_id)
        return appointment

    @jwt_required()
    def delete(self, appointment_id):
        appointment = AppointmentModel.query.get_or_404(appointment_id)
        try:
            db.session.delete(appointment)
            db.session.commit()
            return {"message": "Appointment deleted."}, 200
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while deleting the appointment. {e}")

    @jwt_required()
    @blp.arguments(AppointmentSchema)
    @blp.response(200, AppointmentSchema)
    def put(self, appointment_data, appointment_id):
        appointment = AppointmentModel.query.get(appointment_id)
        if appointment:
            for key, value in appointment_data.items():
                setattr(appointment, key, value)
        else:
            appointment_data["id"] = appointment_id
            appointment = AppointmentModel(**appointment_data)

        try:
            db.session.add(appointment)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while updating the appointment. {e}")

        return appointment
