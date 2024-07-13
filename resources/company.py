# resources/company.py
from flask import request, send_from_directory
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required
from db import db
from models.company import CompanyModel
from schema.company import CompanySchema
from werkzeug.utils import secure_filename
from sqlalchemy import text
from datetime import datetime
import os

blp = Blueprint("Companies", "companies", description="Operations on Companies")

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
company_logo = UPLOAD_FOLDER

@blp.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(company_logo, filename)

def truncate_table():
    try:
        db.session.execute(text('TRUNCATE TABLE companies'))
        db.session.commit()
    except SQLAlchemyError as e:
        abort(500, message=f"An error occurred while truncating the table: {e}")

@blp.route("/company-info")
class CompanyList(MethodView):
    @jwt_required()
    @blp.response(200, CompanySchema)
    def get(self):
        company = CompanyModel.query.first()
        if not company:
            abort(404, message="No company found.")
        return company

    @jwt_required()
    @blp.arguments(CompanySchema, location="form")
    @blp.response(201, CompanySchema)
    def post(self, company_data):
        truncate_table()

        file = request.files.get('logo_path')
        if file:
            filename = secure_filename(file.filename)
            logo_path = os.path.join("uploads/company_logos", filename)
            file.save(logo_path)
        else:
            logo_path = None

        company = CompanyModel(
            name_of_company=company_data["name_of_company"],
            email=company_data["email"],
            phone_number=company_data["phone_number"],
            street_name=company_data["street_name"],
            street_address=company_data["street_address"],
            suite_unit=company_data.get("suite_unit"),
            city=company_data["city"],
            state=company_data["state"],
            logo_path=logo_path
        )
        try:
            db.session.add(company)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the company: {e}")

        return company
