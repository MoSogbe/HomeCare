# resources/administrative_documentation.py
from flask import request, send_from_directory
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required
from db import db
from models.administrative_documentation import AdministrativeDocumentationModel
from models.document_type import DocumentTypeModel
from models.users import UserModel
from schema.administrative_documentation import AdministrativeDocumentationSchema
from werkzeug.utils import secure_filename
from datetime import datetime
import os

blp = Blueprint("AdministrativeDocumentations", "administrative_documentations", description="Operations on Administrative Documentations")
UPLOAD_FOLDER = "uploads/administrative_documentations"

@blp.route("/administrative_documentation")
class AdministrativeDocumentationUpload(MethodView):
    @jwt_required()
    @blp.response(201, AdministrativeDocumentationSchema)
    def post(self):
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

        comment = request.form.get('comment')

        administrative_documentation = AdministrativeDocumentationModel(
            document_type_id=document_type_id,
            created_by=user_id,
            file_path=file_path,
            comment=comment,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        try:
            db.session.add(administrative_documentation)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while saving the administrative documentation: {str(e)}")

        return administrative_documentation

    @jwt_required()
    @blp.response(200, AdministrativeDocumentationSchema(many=True))
    def get(self, participant_id):
        documentations = db.session.query(
            AdministrativeDocumentationModel,
            DocumentTypeModel.document_type,
            UserModel.full_name.label('created_by_full_name')
        ).join(DocumentTypeModel, AdministrativeDocumentationModel.document_type_id == DocumentTypeModel.id)\
         .join(UserModel, AdministrativeDocumentationModel.created_by == UserModel.id)\
         .filter(AdministrativeDocumentationModel.participant_id == participant_id)\
         .all()
        if not documentations:
            abort(404, message="No documentations found for the specified participant.")
        return [
            {
                "id": doc.AdministrativeDocumentationModel.id,
                "document_type_id": doc.AdministrativeDocumentationModel.document_type_id,
                "document_type": doc.document_type,
                "created_by": doc.AdministrativeDocumentationModel.created_by,
                "created_by_full_name": doc.created_by_full_name,
                "file_path": doc.AdministrativeDocumentationModel.file_path,
                "comment": doc.AdministrativeDocumentationModel.comment,
                "created_at": doc.AdministrativeDocumentationModel.created_at,
                "updated_at": doc.AdministrativeDocumentationModel.updated_at,
            }
            for doc in documentations
        ]

    @jwt_required()
    @blp.response(204)
    def delete(self, participant_id):
        documentation_id = request.args.get('documentation_id')
        if not documentation_id:
            abort(400, message="Documentation ID is required.")

        documentation = AdministrativeDocumentationModel.query.get_or_404(documentation_id)

        try:
            db.session.delete(documentation)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while deleting the documentation: {str(e)}")

        return '', 204

@blp.route("/administrative_documentations")
class AllAdministrativeDocumentations(MethodView):
    @jwt_required()
    @blp.response(200, AdministrativeDocumentationSchema(many=True))
    def get(self):
        documentations = db.session.query(
            AdministrativeDocumentationModel,
            DocumentTypeModel.document_type,
            UserModel.full_name.label('created_by_full_name')
        ).join(DocumentTypeModel, AdministrativeDocumentationModel.document_type_id == DocumentTypeModel.id)\
         .join(UserModel, AdministrativeDocumentationModel.created_by == UserModel.id)\
         .all()
        return [
            {
                "id": doc.AdministrativeDocumentationModel.id,
                "document_type_id": doc.AdministrativeDocumentationModel.document_type_id,
                "document_type": doc.document_type,
                "created_by": doc.AdministrativeDocumentationModel.created_by,
                "created_by_full_name": doc.created_by_full_name,
                "file_path": doc.AdministrativeDocumentationModel.file_path,
                "comment": doc.AdministrativeDocumentationModel.comment,
                "created_at": doc.AdministrativeDocumentationModel.created_at,
                "updated_at": doc.AdministrativeDocumentationModel.updated_at,
            }
            for doc in documentations
        ]

@blp.route("/administrative_documentation/file/<int:documentation_id>")
class AdministrativeDocumentationFile(MethodView):
    # @jwt_required()
    def get(self, documentation_id):
        documentation = AdministrativeDocumentationModel.query.get_or_404(documentation_id)
        directory = os.path.dirname(documentation.file_path)
        filename = os.path.basename(documentation.file_path)
        return send_from_directory(directory, filename)
