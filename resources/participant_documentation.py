from flask import request, send_from_directory
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required
from db import db
from models.participant_documentation import ParticipantDocumentationModel
from schema.participant_documentation import ParticipantDocumentationSchema
from werkzeug.utils import secure_filename
from datetime import datetime
import os

blp = Blueprint("ParticipantDocumentations", "participant_documentations", description="Operations on Participant Documentations")
UPLOAD_FOLDER = "uploads/participant_documentations"

@blp.route("/participant_documentation/<int:participant_id>")
class ParticipantDocumentationUpload(MethodView):
    @jwt_required()
    @blp.arguments(ParticipantDocumentationSchema)
    @blp.response(201, ParticipantDocumentationSchema)
    def post(self, participant_id):
        user_id = get_jwt_identity()

        # Handle file upload
        file = request.files.get('file_path')
        if not file:
            abort(400, message="File is required.")

        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        participant_documentation = ParticipantDocumentationModel(
            participant_id=participant_id,
            created_by=user_id,
            document_type_id=request.form.get('document_type_id'),
            file_path=file_path,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        try:
            db.session.add(participant_documentation)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while saving the participant documentation: {str(e)}")

        return participant_documentation

    @jwt_required()
    @blp.response(200, ParticipantDocumentationSchema(many=True))
    def get(self, participant_id):
        participant_documentations = ParticipantDocumentationModel.query.filter_by(participant_id=participant_id).all()
        if not participant_documentations:
            abort(404, message="No participant documentations found for the specified participant.")
        return participant_documentations

@blp.route("/participant_documentations")
class AllParticipantDocumentations(MethodView):
    @jwt_required()
    @blp.response(200, ParticipantDocumentationSchema(many=True))
    def get(self):
        participant_documentations = ParticipantDocumentationModel.query.all()
        return participant_documentations

@blp.route("/participant_documentation/file/<int:participant_documentation_id>")
class ParticipantDocumentationFile(MethodView):
    #@jwt_required()
    def get(self, participant_documentation_id):
        participant_documentation = ParticipantDocumentationModel.query.get_or_404(participant_documentation_id)
        directory = os.path.dirname(participant_documentation.file_path)
        filename = os.path.basename(participant_documentation.file_path)
        return send_from_directory(directory, filename)
