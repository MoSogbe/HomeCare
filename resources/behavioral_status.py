from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_
from models.behavioral_status import BStatusModel
from schemas import BStatusSchema
from datetime import datetime

blp = Blueprint("Behavioral Status", "behavioral_statuses", description="Operations on Behavioral Status")


@blp.route("/behavioral-status/<string:bstatus_id>")
class UserType(MethodView):
    @jwt_required()
    @blp.response(200, BStatusSchema)
    def get(self, bstatus_id):
        bstatus = BStatusModel.query.get_or_404(bstatus_id)
        return bstatus
    @jwt_required()
    def delete(self, bstatus_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privillege is required")
        bstatus = BStatusModel.query.get_or_404(bstatus_id)
        db.session.delete(bstatus)
        db.session.commit()
        return {"message": "Behavioral Status Type deleted."}
    @jwt_required()
    #@blp.arguments(UserTypeUpdateSchema)
    @blp.response(200, BStatusSchema)
    def put(self, bstatus_data, bstatus_id):
        bstatus = BStatusModel.query.get(bstatus_id)

        if bstatus:
            bstatus.status = bstatus_data["status"]
        else:
            bstatus = BStatusModel(id=bstatus_id, **bstatus_data)

        db.session.add(bstatus)
        db.session.commit()

        return bstatus


@blp.route("/behavioral-status")
class UserTypeList(MethodView):
    @jwt_required()
    @blp.response(200, BStatusSchema(many=True))
    def get(self):
        return BStatusModel.query.all()
    @jwt_required()
    @blp.arguments(BStatusSchema)
    @blp.response(201, BStatusSchema)
    def post(self, bstatus_data):
        if BStatusModel.query.filter(
            or_
            (
             BStatusModel.status==bstatus_data["status"],
           
             )).first():
            abort(409, message="A behavioral status with that name already exist")
        bstatus = BStatusModel(
            status = bstatus_data["status"],
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        try:
            db.session.add(bstatus)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the behavioral-status {e}.")

        return bstatus
