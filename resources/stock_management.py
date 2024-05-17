from flask.views import MethodView
from flask import jsonify
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_,join
from models import DrugModel,StockModel,SupplierModel,StockTotalModel,BatchNumModel
from models.medical_information import MedicalInformationModel
from schemas import DrugSchema, SupplierSchema, StockSchema,StockListSchema
from datetime import datetime
import random

blp = Blueprint("Stock Management Model", "stocks", description="Operations on Stock Management Model")

@blp.route("/suppliers/<string:supplier_name>")
class Supplier_Autosuggest(MethodView):
    @jwt_required()
    @blp.response(200, SupplierSchema(many=True))
    def get(self,supplier_name):
        supplier = SupplierModel.query.filter(SupplierModel.supplier_name.ilike(f'%{supplier_name}%')).all()
        supplier_dicts = [{'id': model.id, 'supplier_name': model.supplier_name} for model in supplier]
        return jsonify(supplier_dicts)

@blp.route("/drugs/<string:drug_name>")
class Drugs_Autosuggest(MethodView):
    @jwt_required()
    @blp.response(200, DrugSchema(many=True))
    def get(self,drug_name):
        drugs = DrugModel.query.filter(DrugModel.drug_name.ilike(f'%{drug_name}%')).all()
        drug_dicts = [{'id': model.id, 'drug_name': model.drug_name} for model in drugs]
        return jsonify(drug_dicts)


@blp.route("/stocks/<string:mi_id>")
class MedicalInformationType(MethodView):
    @jwt_required()
    @blp.response(200, StockSchema)
    def get(self, mi_id):
        medical_information = StockSchema.query.get_or_404(mi_id)
        return medical_information
    @jwt_required()
    def delete(self, mi_id):
        jwt = get_jwt()
        # if not jwt.get("is_admin"):
        #     abort(401, message="Admin privillege is required")
        try:
            medical_information = MedicalInformationModel.query.get_or_404(mi_id)
            db.session.delete(medical_information)
            db.session.commit()
            return {"message": "Medical Condition  Type deleted."}
        except SQLAlchemyError as e:
                abort(500, message=f"An error occurred while deleting the Medical Condition. {e}")



    @jwt_required()
    @blp.arguments(StockSchema)
    @blp.response(200, StockSchema)
    def put(self, mi_data, mi_id):
        medical_information = StockModel.query.get(mi_id)

        if medical_information:
            medical_information.supplier_name = mi_data["supplier_name"]
        else:
            medical_information = MedicalInformationModel(id=mi_id, **mi_data)

        db.session.add(medical_information)
        db.session.commit()

        return medical_information


@blp.route("/stocks")
class StocksRoute(MethodView):
    @jwt_required()
    @blp.response(200, StockListSchema(many=True))
    def get(self):
        return  StockModel.query.join(DrugModel, StockModel.drug_id == DrugModel.id).with_entities(StockModel.id,StockModel.transaction_code,StockModel.batch_code,StockModel.supplier_id,StockModel.drug_id,StockModel.quantity_received,StockModel.expiry_date,DrugModel.drug_name).all()

    @jwt_required()
    @blp.arguments(StockSchema)
    @blp.response(201, StockSchema)
    def post(self, stock_data):
        digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        stocks = StockModel(
            transaction_code = stock_data["transaction_code"],
            batch_code = stock_data["batch_code"],
            supplier_id = stock_data["supplier_id"],
            drug_id = stock_data["drug_id"],
            quantity_received = stock_data["quantity_received"],
            expiry_date = stock_data["expiry_date"],
            #created_by = get_jwt_identity(),
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        try:
            db.session.add(stocks)
            db.session.commit()
            # Update StockTotal
            stock_total = StockTotalModel.query.filter_by(drug_id=stock_data["drug_id"]).first()
            if stock_total:
                # Update existing stock total
                stock_total.total_qty = str(int(stock_total.total_qty) + int(stock_data["quantity_received"]))
                stock_total.updated_at = datetime.now()
            # else:
            #     # Create new stock total entry if it doesn't exist
            #     stock_total = StockTotalModel(
            #         total_qty=stock_data["quantity_received"],
            #         drug_id=stock_data["drug_id"],
            #         created_at=datetime.now(),
            #         updated_at=datetime.now()
            #     )
                db.session.add(stock_total)

            db.session.commit()  # Commit the stock total update
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the Stock Information {e}.")

        return stocks
