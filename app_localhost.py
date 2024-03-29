from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
import models
import secrets
import os
import redis
from rq import Queue
from db import db
from dotenv import load_dotenv 
from resources.users import blp as UserBlueprint
from resources.user_types import blp as UserTypeBlueprint
from resources.company import blp as CompanyBlueprint
from resources.service_category import blp as ServiceCategoryBlueprint
from resources.services import blp as ServicesBlueprint
from resources.uom import blp as UOMBlueprint
from blocklist import BLOCKLIST
from flask_migrate import Migrate
from flask_cors import CORS

def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()
    
    CORS(app, resources={ r'/*': {'origins': '*'}})
    app.config["API_TITLE"] = "HomeCare API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL",f"mysql://root:123456@localhost/homecare")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.debug = True
    db.init_app(app)
    migrate = Migrate(app,db)
    api = Api(app)
    app.config["JWT_SECRET_KEY"] = "brownfoxjumponthewall"
    jwt=JWTManager(app)
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header,jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return(
            jsonify(
                {"description": "The token has beed revoked", "error":"token_revoked"}
            ),
            401,
        )
        
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header,jwt_payload):
        return (
            jsonify(
                {"description": "The token is not fresh", "error":"fresh_tokn_required"}
            ),
            401,
        )
    
    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity==1:
            return {"is_admin" : True}
        return {"is_admin":False}
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )
        
   
    api.register_blueprint(UserTypeBlueprint)
    api.register_blueprint(CompanyBlueprint)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(ServiceCategoryBlueprint)
    api.register_blueprint(ServicesBlueprint)
    api.register_blueprint(UOMBlueprint)
   
    return app
