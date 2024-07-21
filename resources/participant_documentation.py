from flask import request, send_from_directory
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required
from db import db
from models.participant_documentation import ParticipantDocumentationModel
from models.document_type import DocumentTypeModel
from models.users import UserModel
from schema.participant_documentation import ParticipantDocumentationSchema
from werkzeug.utils import secure_filename
from datetime import datetime
import os

blp = Blueprint("ParticipantDocumentations", "participant_documentations", description="Operations on Participant Documentations")
UPLOAD_FOLDER = "uploads/participant_documentations"

@blp.route("/participant_documentation/<int:participant_id>")
class ParticipantDocumentationUpload(MethodView):
    @jwt_required()
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

        document_type_id = request.form.get('document_type_id')
        if not document_type_id:
            abort(400, message="Document type is required.")

        participant_documentation = ParticipantDocumentationModel(
            participant_id=participant_id,
            document_type_id=document_type_id,
            created_by=user_id,
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
        documentations = db.session.query(
            ParticipantDocumentationModel,
            DocumentTypeModel.document_type,
            UserModel.fullname.label('created_by_full_name')
        ).join(DocumentTypeModel, ParticipantDocumentationModel.document_type_id == DocumentTypeModel.id)\
         .join(UserModel, ParticipantDocumentationModel.created_by == UserModel.id)\
         .filter(ParticipantDocumentationModel.participant_id == participant_id)\
         .all()
        if not documentations:
            abort(404, message="No documentations found for the specified participant.")
        return [
            {
                "id": doc.ParticipantDocumentationModel.id,
                "participant_id": doc.ParticipantDocumentationModel.participant_id,
                "document_type_id": doc.ParticipantDocumentationModel.document_type_id,
                "document_type": doc.document_type,
                "created_by": doc.ParticipantDocumentationModel.created_by,
                "created_by_full_name": doc.created_by_full_name,
                "file_path": doc.ParticipantDocumentationModel.file_path,
                "created_at": doc.ParticipantDocumentationModel.created_at,
                "updated_at": doc.ParticipantDocumentationModel.updated_at,
            }
            for doc in documentations
        ]

@blp.route("/participant_documentations")
class AllParticipantDocumentations(MethodView):
    @jwt_required()
    @blp.response(200, ParticipantDocumentationSchema(many=True))
    def get(self):
        documentations = db.session.query(
            ParticipantDocumentationModel,
            DocumentTypeModel.document_type,
            UserModel.fullname.label('created_by_full_name')
        ).join(DocumentTypeModel, ParticipantDocumentationModel.document_type_id == DocumentTypeModel.id)\
         .join(UserModel, ParticipantDocumentationModel.created_by == UserModel.id)\
         .all()
        return [
            {
                "id": doc.ParticipantDocumentationModel.id,
                "participant_id": doc.ParticipantDocumentationModel.participant_id,
                "document_type_id": doc.ParticipantDocumentationModel.document_type_id,
                "document_type": doc.document_type,
                "created_by": doc.ParticipantDocumentationModel.created_by,
                "created_by_full_name": doc.created_by_full_name,
                "file_path": doc.ParticipantDocumentationModel.file_path,
                "created_at": doc.ParticipantDocumentationModel.created_at,
                "updated_at": doc.ParticipantDocumentationModel.updated_at,
            }
            for doc in documentations
        ]

@blp.route("/participant_documentation/file/<int:documentation_id>")
class ParticipantDocumentationFile(MethodView):
    # @jwt_required()
    def get(self, documentation_id):
        documentation = ParticipantDocumentationModel.query.get_or_404(documentation_id)
        directory = os.path.dirname(documentation.file_path)
        filename = os.path.basename(documentation.file_path)
        return send_from_directory(directory, filename)
