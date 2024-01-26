from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_
from models.participant import ParticipantModel
from schemas import ParticipantSchema
from datetime import datetime

blp = Blueprint("Participant Profile", "participants", description="Operations on Profile Profile")

@blp.route("/participants/<string:participant_id>")
class ParticipantType(MethodView):
    @jwt_required()
    @blp.response(200, ParticipantSchema)
    def get(self, participant_id):
        participant = ParticipantModel.query.get_or_404(participant_id)
        return participant
    @jwt_required()
    def delete(self,participant_id):
        jwt = get_jwt()
        # if not jwt.get("is_admin"):
        #     abort(401, message="Admin privillege is required")
        try:
            participant = ParticipantModel.query.get_or_404(participant_id)
            db.session.delete(participant)
            db.session.commit()
            return {"message": "Staff Profile Type deleted."}
        except SQLAlchemyError as e:
                abort(500, message=f"An error occurred while deleting the staff profile. {e}")
    
   
    @jwt_required()
    @blp.arguments(ParticipantSchema)
    @blp.response(200, ParticipantSchema)
    def put(self, participant_data, participant_id):
        participant = ParticipantModel.query.get(participant_id)

        if participant:
            participant.name = participant_data["name"]
        else:
            participant = ParticipantModel(id=participant_id, **participant_data)

        db.session.add(participant)
        db.session.commit()

        return participant


@blp.route("/participants")
class ParticipantList(MethodView):
    @jwt_required()
    @blp.response(200, ParticipantSchema(many=True))
    def get(self):
        return ParticipantModel.query.all()
    @jwt_required()
    @blp.arguments(ParticipantSchema)
    @blp.response(201, ParticipantSchema)
    def post(self, participant_data):
       
        if ParticipantModel.query.filter(
            or_
            (
             ParticipantModel.name==participant_data["name"],
           
             )).first():
            abort(409, message="A staff with that name already exist")
            # Handle photo upload
       
        
         
        photo = request.form.get('profile_image')
        
            # Create a ParticipantModel instance
        participant = ParticipantModel(
            name=participant_data["name"],
            dob=participant_data["dob"],
            ssn=participant_data["ssn"],
            maid_number=participant_data["maid_number"],
            legal_status=participant_data["legal_status"],
            home_address=participant_data["home_address"],
            home_phone=participant_data["home_phone"],
            gender_id=participant_data["gender_id"],
            bio_title_id=participant_data["bio_title_id"],
            profile_image=participant_data["profile_image"],
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        try:
            if photo:
                photo.save('uploads/' + photo.filename)
            db.session.add(participant)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the participant .{e}.")
        return participant
