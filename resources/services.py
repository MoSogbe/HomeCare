from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_
from models.service import ServiceModel
from schemas import ServiceSchema,ServiceUpdateSchema
from datetime import datetime

blp = Blueprint("Services", "user_types", description="Operations on services being rendered in the care home")


@blp.route("/services/<string:service_id>")
class UserType(MethodView):
    @jwt_required()
    @blp.response(200, ServiceSchema)
    def get(self, service_id):
        services = ServiceModel.query.get_or_404(service_id)
        return services
    @jwt_required()
    def delete(self, service_id):
        jwt = get_jwt()
        # if not jwt.get("is_admin"):
        #     abort(401, message="Admin privillege is required")
       
        try:
            services = ServiceModel.query.get_or_404(service_id)
            db.session.delete(services)
            db.session.commit()
            return {"message": "Service Type deleted."}
    
        except SQLAlchemyError as e:
                abort(500, message=f"An error occurred while inserting the services. {e}")
    
    @jwt_required()
    @blp.arguments(ServiceUpdateSchema)
    @blp.response(200, ServiceSchema)
    def put(self, service_data, service_id):
        services = ServiceModel.query.get(service_id)
        if services:
            services.service_name = service_data["service_name"]
            services.service_price = service_data["service_price"],
            services.service_charge_duration = service_data["service_charge_duration"],
            services.service_charge_frequency = service_data["service_charge_frequency"],
            services.service_category = service_data["service_category"],
        else:
            services = ServiceModel(id=service_id, **service_data)
            

        db.session.add(services)
        db.session.commit()

        return services


@blp.route("/services")
class ServiceList(MethodView):
    @jwt_required()
    @blp.response(200, ServiceSchema(many=True))
    def get(self):
        return ServiceModel.query.all()
    @jwt_required()
    @blp.arguments(ServiceSchema)
    @blp.response(201, ServiceSchema)
    def post(self, service_data):
        if ServiceModel.query.filter(
            or_
            (
             ServiceModel.service_name==service_data["service_name"],
           
             )).first():
            abort(409, message="A service Type with that name already exist")
        services = ServiceModel(
            service_name = service_data["service_name"],
            service_price = service_data["service_price"],
            service_charge_duration = service_data["service_charge_duration"],
            service_charge_frequency = service_data["service_charge_frequency"],
            service_category = service_data["service_category"],
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        try:
            db.session.add(services)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the services. {e}")

        return services
