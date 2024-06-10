from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_
from models.participant import ParticipantModel
from models.daily_notes import DailyNotesModel
from schemas import ParticipantSchema, PrescriptionSchema,PrescriptionUpdateSchema
from schema.daily_notes import DailyNoteSchema
from datetime import datetime

blp = Blueprint("Participant Daily Note", "daily_notes", description="Operations on Participant Daily Note")

@blp.route("/daily-note/<string:participant>")
class VitalsGet(MethodView):
    @jwt_required()
    @blp.response(200, DailyNoteSchema(many=True))
    def get(self, participant):
        participant =  DailyNotesModel.query.filter_by(participant_id=participant).all()
        return participant


@blp.route("/daily-note")
class VitalsPost(MethodView):
    @jwt_required()
    @blp.arguments(DailyNoteSchema)
    @blp.response(201, DailyNoteSchema)
    def post(self, vitals_data):

        # Create a PrescriptionModel instance
        vitals = DailyNotesModel(
            participant_id=vitals_data["participant_id"],
            comment=vitals_data["comment"],
            created_by=get_jwt_identity(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        try:
            db.session.add(vitals)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the participant vitals .{e}.")
        return vitals
