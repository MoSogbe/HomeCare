from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from datetime import datetime
import requests
import os
from flask import current_app
from sqlalchemy import or_
from db import db
from models import  UserModel
from schemas import UserSchema, UserRegistersSchema
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity, get_jwt,jwt_required
from blocklist import BLOCKLIST

blp = Blueprint("Users", "users", description="Operations  on user model")


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username==user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            user_type = user.user_type
            return {"access_token": access_token, "refresh_token" : refresh_token, "user_type":user_type}
        abort(401,message="Invalid Credentials")

@blp.route("/refresh")
class   TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        
        return {"access_token": new_token}
        
    

@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message":"Successfully logged out"}


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserRegistersSchema)
    def post(self, user_data):
        if UserModel.query.filter(
            or_
            (
             UserModel.username==user_data["username"],
             UserModel.email == user_data["email"]
             )).first():
            abort(409, message="A user with that name already exist")
        user = UserModel(
            fullname = user_data["fullname"],
            username = user_data["username"],
            email = user_data["email"],
            user_type = user_data["user_type"],
            password = pbkdf2_sha256.hash(user_data["password"]),
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        db.session.add(user)
        db.session.commit()
        
               
        return {"message": "User created successfully"}, 201

@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200        
        