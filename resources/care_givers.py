from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_
from models.care_giver import CareGiverModel
from schemas import StaffSchema
from datetime import datetime

blp = Blueprint("Staff Profile", "care_givers", description="Operations on Staff Profile")

@blp.route("/staff-profile/<string:staff_id>")
class StaffType(MethodView):
    @jwt_required()
    @blp.response(200, StaffSchema)
    def get(self, care_giver_id):
        care_giver = CareGiverModel.query.get_or_404(care_giver_id)
        return care_giver
    @jwt_required()
    def delete(self,care_giver_id):
        jwt = get_jwt()
        # if not jwt.get("is_admin"):
        #     abort(401, message="Admin privillege is required")
        try:
            btitle = CareGiverModel.query.get_or_404(care_giver_id)
            db.session.delete(btitle)
            db.session.commit()
            return {"message": "Staff Profile Type deleted."}
        except SQLAlchemyError as e:
                abort(500, message=f"An error occurred while deleting the staff profile. {e}")
    
   
    @jwt_required()
    @blp.arguments(StaffSchema)
    @blp.response(200, StaffSchema)
    def put(self, care_giver_data, staff_id):
        care_giver = CareGiverModel.query.get(staff_id)

        if care_giver:
            care_giver.name = care_giver_data["name"]
        else:
            care_giver = CareGiverModel(id=staff_id, **care_giver_data)

        db.session.add(care_giver)
        db.session.commit()

        return care_giver


@blp.route("/staff-profile")
class StaffList(MethodView):
    @jwt_required()
    @blp.response(200, StaffSchema(many=True))
    def get(self):
        return CareGiverModel.query.all()
    @jwt_required()
    @blp.arguments(StaffSchema)
    @blp.response(201, StaffSchema)
    def post(self, staff_data):
       
        if CareGiverModel.query.filter(
            or_
            (
             CareGiverModel.name==staff_data["name"],
           
             )).first():
            abort(409, message="A staff with that name already exist")
            # Handle photo upload
       
        
         
        photo = request.form.get('profile_image')
        
            # Create a CaregiverModel instance
        staff = CareGiverModel(
            name=staff_data["name"],
            email=staff_data["email"],
            phone=staff_data["phone"],
            address=staff_data["address"],
            location=staff_data["location"],
            gender_id=staff_data["gender_id"],
            bio_title_id=staff_data["bio_title_id"],
            user_id=staff_data["user_id"],
            profile_image=staff_data["profile_image"],
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        try:
            if photo:
                photo.save('uploads/' + photo.filename)
            db.session.add(staff)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the staff .{e}.")
        return staff
