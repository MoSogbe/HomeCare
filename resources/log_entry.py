from flask import request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from db import db
from flask_smorest import Blueprint, abort
from sqlalchemy.orm import aliased
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from models import LogEntryModel, ParticipantModel, CareGiverModel, ServiceModel
from schema.log_entry import LogEntrySchema,LogEntryUpdateSchema

log_entry_blp = Blueprint(
    'Log Entry', 'log_entry', url_prefix='/log-entries',
    description="Operations on Log Entries"
)

@log_entry_blp.route("")
class LogEntryList(MethodView):
    @jwt_required()
    @log_entry_blp.response(200, LogEntrySchema(many=True))
    def get(self):
        results = db.session.query(
            LogEntryModel.id,
            LogEntryModel.participant_id,
            LogEntryModel.user_id,
            LogEntryModel.check_in,
            LogEntryModel.check_out,
            LogEntryModel.notes,
            LogEntryModel.service_id
        ).all()

        log_entries = [{
            'id': r.id,
            'participant_id': r.participant_id,
            'user_id': r.user_id,
            'check_in': r.check_in,
            'check_out': r.check_out,
            'notes': r.notes,
            'service_id': r.service_id
        } for r in results]

        return jsonify(log_entries)

    @jwt_required()
    @log_entry_blp.arguments(LogEntrySchema)
    @log_entry_blp.response(201, LogEntrySchema)
    def post(self, log_entry_data):
        log_entry = LogEntryModel(
            participant_id=log_entry_data['participant_id'],
            check_in=log_entry_data['check_in'],
            check_out=log_entry_data.get('check_out'),
            notes=log_entry_data.get('notes'),
            service_id=log_entry_data.get('service_id'),
            user_id = log_entry_data.get('user_id')
        )

        try:
            db.session.add(log_entry)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while inserting the log entry: {e}")

        return jsonify(LogEntrySchema().dump(log_entry)), 201

@log_entry_blp.route("/<int:log_entry_id>")
class LogEntryDetail(MethodView):
    @jwt_required()
    @log_entry_blp.response(200, LogEntrySchema)
    def get(self, log_entry_id):
        log_entry = LogEntryModel.query.get_or_404(log_entry_id)
        return jsonify(LogEntrySchema().dump(log_entry))

    @jwt_required()
    @log_entry_blp.arguments(LogEntryUpdateSchema)
    @log_entry_blp.response(200, LogEntrySchema)
    def put(self, log_entry_data, log_entry_id):
        log_entry = LogEntryModel.query.get_or_404(log_entry_id)

        log_entry.participant_id = log_entry_data.get('participant_id', log_entry.participant_id)
        log_entry.caregiver_id = log_entry_data.get('user_id', log_entry.caregiver_id)
        log_entry.check_in = log_entry_data.get('check_in', log_entry.check_in)
        log_entry.check_out = log_entry_data.get('check_out', log_entry.check_out)
        log_entry.notes = log_entry_data.get('notes', log_entry.notes)
        log_entry.service_id = log_entry_data.get('service_id', log_entry.service_id)

        try:
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while updating the log entry: {e}")

        return jsonify(LogEntrySchema().dump(log_entry))

    @jwt_required()
    @log_entry_blp.response(204)
    def delete(self, log_entry_id):
        log_entry = LogEntryModel.query.get_or_404(log_entry_id)

        try:
            db.session.delete(log_entry)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while deleting the log entry: {e}")

        return '', 204


@log_entry_blp.route("/participant/<int:participant_id>")
class LogEntriesByParticipant(MethodView):
    @jwt_required()
    @log_entry_blp.response(200, LogEntrySchema(many=True))
    def get(self, participant_id):
        try:
            log_entries = LogEntryModel.query.filter_by(participant_id=participant_id).all()
            if not log_entries:
                abort(404, message="No log entries found for the specified participant.")
            return log_entries
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while retrieving log entries: {str(e)}")
