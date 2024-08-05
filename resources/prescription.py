from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from db import db
from sqlalchemy import or_, and_
from models.participant import ParticipantModel
from models.prescription import PrescriptionModel
from models.mar_administration import AdministrationModel
from models.med_action import MedActionModel
from models.users import UserModel
from schema.med_action import MedActionSchema
from schema.med_action_status import MedActionStatusSchema
from models.stock_total import StockTotalModel
from schemas import ParticipantSchema, PrescriptionSchema, PrescriptionUpdateSchema, PrescriptionQuerySchema
from schema.give import GiveSchema
from datetime import datetime, date


blp = Blueprint("Participant Prescription", "prescriptions", description="Operations on Participant Prescription or MAR")

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

def reset_todays_frequency():
    today = date.today()
    prescriptions = PrescriptionModel.query.all()
    for prescription in prescriptions:
        # Convert the date_from and date_to strings to datetime objects
        date_from = datetime.strptime(prescription.date_from, '%Y-%m-%d %H:%M:%S')
        date_to = datetime.strptime(prescription.date_to, '%Y-%m-%d %H:%M:%S')

        if date_from.date() <= today <= date_to.date():
            prescription.todays_frequency = prescription.frequency
    db.session.commit()

@blp.route("/mar/<int:participant_id>")
class MarType(MethodView):
    @jwt_required()
    #@blp.arguments(PrescriptionQuerySchema)
    @blp.response(200, PrescriptionSchema(many=True))
    def get(self, participant_id):
        now = datetime.now()
        date_from = datetime(now.year, now.month, now.day, 0, 0, 1)
        date_to = datetime(now.year, now.month, now.day, 23, 59, 59)

        if not date_from or not date_to:
            abort(400, message="date_from and date_to query parameters are required.")

        try:
            reset_todays_frequency()  # Reset today's frequency at the start of each day

            query = PrescriptionModel.query.filter(
                PrescriptionModel.participant_id == participant_id,
                PrescriptionModel.date_from <= date_to,
                PrescriptionModel.date_to >= date_from
            )
            prescriptions = query.all()

            if not prescriptions:
                abort(404, message="No prescriptions found for the specified participant and date range.")

            return prescriptions
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while retrieving prescriptions: {str(e)}")

@blp.route("/mar/<string:mar_id>")
class MarUpdate(MethodView):
    @jwt_required()
    def delete(self, mar_id):
        jwt = get_jwt()
        try:
            participant_mar = PrescriptionModel.query.get_or_404(mar_id)
            db.session.delete(participant_mar)
            db.session.commit()
            return {"message": "Participant Prescription deleted."}
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while deleting the Participant Prescription. {e}")

    @jwt_required()
    @blp.arguments(PrescriptionUpdateSchema)
    @blp.response(200, PrescriptionUpdateSchema)
    def put(self, participant_data, mar_id):
        mar = PrescriptionModel.query.get(mar_id)
        if mar is None:
            return {"error": "Prescription not found"}, 404

        for key, value in participant_data.items():
            setattr(mar, key, value)

        mar.updated_at = datetime.now()
        if 'created_at' in participant_data:
            mar.created_at = participant_data['created_at']

        db.session.commit()
        return mar

@blp.route("/mars")
class MarPost(MethodView):
    @jwt_required()
    @blp.arguments(PrescriptionSchema)
    @blp.response(201, PrescriptionSchema)
    def post(self, participant_data):
        participant = PrescriptionModel(
            participant_id=participant_data["participant_id"],
            drug_id=participant_data["drug_id"],
            reason_for_medication=participant_data["reason_for_medication"],
            mar_date=participant_data["mar_date"],
            mar_time=participant_data["mar_time"],
            date_from=participant_data["date_from"],
            date_to=participant_data["date_to"],
            place_of_mar=participant_data["place_of_mar"],
            dossage=participant_data["dossage"],
            frequency=participant_data["frequency"],
            todays_frequency=participant_data["frequency"],  # Set today's frequency
            qty=participant_data["qty"],
            comment=participant_data["comment"],
            created_by=get_jwt_identity(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        try:
            db.session.add(participant)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the participant prescription: {e}.")
        return participant

@blp.route("/mar/give/<int:mar_id>")
class MarGive(MethodView):
    @jwt_required()
    @blp.arguments(GiveSchema)
    def post(self,give_data, mar_id):
        if not request.is_json:
            abort(415, message="Content-Type must be application/json")

        status_id = give_data.get('status_id')
        if status_id is None:
            abort(400, message="status_id is required")

        try:
            prescription = PrescriptionModel.query.get_or_404(mar_id)
            today = date.today()

            # Convert the date_from and date_to strings to datetime objects
            date_from = parse_date(prescription.date_from)
            date_to = parse_date(prescription.date_to)

            if date_from.date() <= today <= date_to.date():
                if prescription.todays_frequency < prescription.frequency:
                    # Get the stock for the drug
                    stock = StockTotalModel.query.filter_by(drug_id=prescription.drug_id).first()

                    if stock is None:
                        return {"message": "No stock found for this drug."}, 400

                    stock_qty = int(stock.total_qty)
                    if stock_qty < prescription.qty:
                        return {"message": "Not enough stock available for this drug."}, 400

                    if status_id != 1:
                        # Save the action in the med action table
                        med_action = MedActionModel(
                            mar_id=prescription.id,
                            status_id=status_id,
                            administered_by=get_jwt_identity(),
                            created_at=datetime.now()
                        )
                        db.session.add(med_action)
                        db.session.commit()
                        return {"message": "Medication action recorded successfully."}, 200
                    else:
                        # Deduct the quantity from the stock
                        stock.total_qty = str(stock_qty - prescription.qty)
                        stock.updated_at = datetime.now()

                        administration = AdministrationModel(
                            mar_id=prescription.id,
                            administered_by=get_jwt_identity()
                        )
                        db.session.add(administration)
                        prescription.todays_frequency += 1
                        prescription.updated_at = datetime.now()

                        db.session.commit()
                        return {
                            "message": "Medication given successfully.",
                            "remaining_frequency": prescription.todays_frequency,
                            "remaining_stock": stock.total_qty
                        }, 200
                else:
                    return {"message": "No remaining frequency for this medication today."}, 400
            else:
                return {"message": "This prescription is not valid today."}, 400
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while updating the prescription: {str(e)}")


@blp.route("/med_actions")
class MedActionList(MethodView):
    @blp.response(200, MedActionSchema(many=True))
    def get(self):
        try:
            med_actions = db.session.query(
                MedActionModel,
                ParticipantModel.name.label("participant_name"),
                UserModel.fullname.label("caregiver_name"),
                MedActionModel.status_name.label("status")
            ).join(ParticipantModel, MedActionModel.mar_id == ParticipantModel.id)\
             .join(UserModel, MedActionModel.administered_by == UserModel.id)\
             .join(MedActionModel, MedActionModel.status_id == MedActionModel.id)\
             .all()

            if not med_actions:
                abort(404, message="No medication actions found.")

            return [
                {
                    "id": action.MedActionModel.id,
                    "mar_id": action.MedActionModel.mar_id,
                    "status_id": action.MedActionModel.status_id,
                    "status": action.status,
                    "administered_by": action.MedActionModel.administered_by,
                    "caregiver_name": action.caregiver_name,
                    "participant_name": action.participant_name,
                    "created_at": action.MedActionModel.created_at,
                }
                for action in med_actions
            ]
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while retrieving medication actions: {str(e)}")
