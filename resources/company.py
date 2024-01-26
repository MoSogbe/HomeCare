from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_
from models.company import CompanyModel
from schemas import CompanySchema
from datetime import datetime

blp = Blueprint("Company Info", "compnaies", description="Operations on Company Profile")


@blp.route("/company-info")
class CompanyList(MethodView):
    @jwt_required()
    @blp.response(200, CompanySchema(many=False))
    def get(self):
        first_company = CompanyModel.query.first()
        return first_company
    @jwt_required()
    @blp.arguments(CompanySchema)
    @blp.response(201, CompanySchema)
    def post(self, company_data):
        
        company = CompanyModel(
            name_of_company = company_data["name_of_company"],
            email = company_data["email"],
            phone_number = company_data["phone_number"],
            address = company_data["address"],
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        try:
            record_to_delete = CompanyModel.query.first()
            if record_to_delete:
                db.session.delete(record_to_delete)
                db.session.commit()
            db.session.add(company)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the company info.{e}")

        return company
