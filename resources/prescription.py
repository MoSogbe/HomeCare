from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_
from models.participant import ParticipantModel
from models.prescription import PrescriptionModel
from schemas import ParticipantSchema, PrescriptionSchema,PrescriptionUpdateSchema
from datetime import datetime

blp = Blueprint("Participant Prescription", "prescriptions", description="Operations on Participant Prescription or MAR")

@blp.route("/mar/<string:participant_id>")
class MarType(MethodView):
    @jwt_required()
    @blp.response(200, PrescriptionSchema(many=True))
    def get(self, participant_id):
        participant = PrescriptionModel.query.filter_by(participant_id=participant_id).all()
        return participant
@blp.route("/mar/<string:mar_id>")
class MarUpdate(MethodView):
    @jwt_required()
    def delete(self,mar_id):
        jwt = get_jwt()
        # if not jwt.get("is_admin"):
        #     abort(401, message="Admin privillege is required")
        try:
            participant_mar = PrescriptionModel.query.get_or_404(mar_id)
            db.session.delete(participant_mar)
            db.session.commit()
            return {"message": "Participant Prescription  deleted."}
        except SQLAlchemyError as e:
                abort(500, message=f"An error occurred while deleting the Participant Prescription. {e}")


    @jwt_required()
    @blp.arguments(PrescriptionUpdateSchema)
    @blp.response(200, PrescriptionUpdateSchema)
    def put(self, participant_data, mar_id):
        mar = PrescriptionModel.query.get(mar_id)
        # Check if the instance exists
        if mar is None:
            return {"error": "Prescription not found"}, 404
        # Update the instance fields with participant_data
        for key, value in participant_data.items():
            setattr(mar, key, value)
        # Set the updated_at field to the current time
        mar.updated_at = datetime.now()
        # Optionally update created_at if it's part of participant_data
        if 'created_at' in participant_data:
            mar.created_at = participant_data['created_at']
        # Commit the changes to the database
        db.session.commit()
        return mar


@blp.route("/mars")
class MarPost(MethodView):
    @jwt_required()
    @blp.arguments(PrescriptionSchema)
    @blp.response(201, PrescriptionSchema)
    def post(self, participant_data):

        # Create a PrescriptionModel instance
        participant = PrescriptionModel(
            participant_id=participant_data["participant_id"],
            drug_id=participant_data["drug_id"],
            reason_for_medication=participant_data["reason_for_medication"],
            mar_date=participant_data["mar_date"],
            mar_time=participant_data["mar_time"],
            date_from=participant_data["date_from"],
            date_to=participant_data["date_to"],
            place_of_mar=participant_data["place_of_mar"],
            dossage=participant_data["dossage"],
            comment=participant_data["comment"],
            created_by=get_jwt_identity(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        try:
            db.session.add(participant)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the participant prescription .{e}.")
        return participant
