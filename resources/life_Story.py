from flask.views import MethodView
from flask import jsonify
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_
from models.mit import MITModel
from models import ECIModel,CaseManagerModel, DiagnosisModel, MedicalInformationModel,ParticipantServiceProviderHistoryModel,PPModel,PHModel,MedicalConditionModel
from schemas import ECISchema
from datetime import datetime

blp = Blueprint("Face Sheet Information", "eci", description="Operations on Face Sheet")


@blp.route("/face-sheet/participant/<string:participant_id>")
class ECIList(MethodView):
    @jwt_required()
    @blp.response(200, ECISchema(many=True))
    def get(self,participant_id):
        life_story_data = []
        eci =  ECIModel.query.filter_by(participant_id=participant_id).all()
        case_manager = CaseManagerModel.query.filter_by(participant_id=participant_id).all()
        diagnosis = DiagnosisModel.query.filter_by(participant_id=participant_id).all()
        mi = MedicalInformationModel.query.join(MedicalConditionModel, MedicalInformationModel.medical_condition_id == MedicalConditionModel.id)\
                               .with_entities(MedicalInformationModel.id, MedicalInformationModel.medical_condition_id, MedicalConditionModel.condition_name)\
                               .filter_by(participant_id=participant_id)\
                               .all()
        psph = ParticipantServiceProviderHistoryModel.query.filter_by(participant_id=participant_id).all()
        pp = PPModel.query.filter_by(participant_id=participant_id).all()
        ph = PHModel.query.filter_by(participant_id=participant_id).all()
        
        case_manager_serialized = [item.serialize() for item in case_manager]
        diagnosis_serialized = [item.serialize() for item in diagnosis]
        eci_serialized = [item.serialize() for item in eci]
        mi_serialized = [item.serialize() for item in mi]
        psph_serialized = [item.serialize() for item in psph]
        pp_serialized = [item.serialize() for item in pp]
        ph_serialized = [item.serialize() for item in ph]
        
        life_story_data.append({"case_manager":case_manager_serialized,"diagnosis":diagnosis_serialized, "emergency_contact_information":eci_serialized , "medical_information":mi_serialized, "participant_service_provider_history": psph_serialized, "participant_physician": pp_serialized, "preferred_hospital" : ph_serialized})
        return jsonify(life_story_data)
 