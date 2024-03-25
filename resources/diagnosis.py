from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_
from models.diagnosis import DiagnosisModel
from schemas import DiagnosisSchema
from datetime import datetime

blp = Blueprint("Diagnosis Model", "diagnosis", description="Operations on Diagnosis Model")


@blp.route("/diagnosis/<string:diagnosis_id>")
class DiagnosisType(MethodView):
    @jwt_required()
    @blp.response(200, DiagnosisSchema)
    def get(self, diagnosis_id):
        diagnosis = DiagnosisModel.query.get_or_404(diagnosis_id)
        return diagnosis
    @jwt_required()
    def delete(self, diagnosis_id):
        jwt = get_jwt()
        # if not jwt.get("is_admin"):
        #     abort(401, message="Admin privillege is required")
        try:
            diagnosis = DiagnosisModel.query.get_or_404(diagnosis_id)
            db.session.delete(diagnosis)
            db.session.commit()
            return {"message": "Diagnosis  Type deleted."}
        except SQLAlchemyError as e:
                abort(500, message=f"An error occurred while deleting the Diagnosis. {e}")
    
    

    @jwt_required()
    @blp.arguments(DiagnosisSchema)
    @blp.response(200, DiagnosisSchema)
    def put(self, diagnosis_data, diagnosis_id):
        diagnosis = DiagnosisModel.query.get(diagnosis_id)

        if diagnosis:
            diagnosis.medication_condition_id = diagnosis_data["medication_condition_id"]
        else:
            diagnosis = DiagnosisModel(id=diagnosis_id, **diagnosis_data)

        db.session.add(diagnosis)
        db.session.commit()

        return diagnosis


@blp.route("/diagnosis/participant/<string:participant_id>")
class DiagnosisGetUser(MethodView):
    @jwt_required()
    @blp.response(200, DiagnosisSchema(many=True))
    def get(self,participant_id):
        return DiagnosisModel.query.filter_by(participant_id=participant_id).all()
    
@blp.route("/diagnosis")
class DiagnosisRoute(MethodView):
    @jwt_required()
    @blp.arguments(DiagnosisSchema)
    @blp.response(201, DiagnosisSchema)
    def post(self, diagnosis_data):
        
        diagnosis = DiagnosisModel(
            participant_id = diagnosis_data["participant_id"],
            medication_condition_id = diagnosis_data["medication_condition_id"],
            created_by = get_jwt_identity(),
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        try:
            db.session.add(diagnosis)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the Diagnosis {e}.")

        return diagnosis
