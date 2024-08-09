from datetime import datetime, date

from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy import and_, extract
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.behavioral_issues import BIssuesModel
from models.participant import ParticipantModel  # Assuming you have a ParticipantModel
from schema.behavioral_issues import BehavioralIssuesSchema, BehavioralIssuesResponseSchema

blp = Blueprint("Behavioral Issues", "behavioral_issues", description="Operations on behavioral_issues")


def get_participant_or_404(participant_id):
    """
    Helper function to check if the participant exists and belongs to the user.
    """
    participant = ParticipantModel.query.filter_by(id=participant_id).first()
    if not participant:
        abort(404, message="Participant not found.")
    return participant


@blp.route("/behavioral_issues/participant/<int:participant_id>")
class BehavioralIssuesList(MethodView):
    @jwt_required()
    @blp.response(200, BehavioralIssuesResponseSchema(many=True))
    def get(self, participant_id):
        """Get behavioral issues for a specific participant."""
        user_id = get_jwt_identity()

        get_participant_or_404(participant_id)

        behavioral_issues = BIssuesModel.query.filter_by(participant_id=participant_id, created_by=user_id).all()
        return behavioral_issues

    @jwt_required()
    @blp.arguments(BehavioralIssuesSchema)
    @blp.response(201, BehavioralIssuesResponseSchema)
    def post(self, behavioral_issues_data, participant_id):
        """Create a behavioral issue for a specific participant, restricted to one per day."""
        user_id = get_jwt_identity()
        today = date.today()

        get_participant_or_404(participant_id)

        existing_issue = BIssuesModel.query.filter(
            and_(
                BIssuesModel.participant_id == participant_id,
                BIssuesModel.created_by == user_id,
                BIssuesModel.created_at >= today
            )
        ).first()

        if existing_issue:
            abort(400, message="An issue has already been reported for this participant today.")

        behavioral_issues_data['created_by'] = user_id
        behavioral_issues_data['participant_id'] = participant_id
        behavioral_issue = BIssuesModel(**behavioral_issues_data)
        try:
            db.session.add(behavioral_issue)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while creating the behavioral issue. {e}")
        return behavioral_issue


@blp.route("/behavioral_issues/<int:issue_id>")
class BehavioralIssueResource(MethodView):
    @jwt_required()
    @blp.response(200, BehavioralIssuesResponseSchema)
    def get(self, issue_id):
        """Get a specific behavioral issue by issue ID."""
        user_id = get_jwt_identity()
        behavioral_issue = BIssuesModel.query.filter_by(id=issue_id, created_by=user_id).first_or_404()
        return behavioral_issue

    @jwt_required()
    @blp.arguments(BehavioralIssuesSchema)
    @blp.response(200, BehavioralIssuesResponseSchema)
    def put(self, behavioral_issues_data, issue_id):
        """Update a specific behavioral issue by issue ID."""
        user_id = get_jwt_identity()
        behavioral_issue = BIssuesModel.query.filter_by(id=issue_id, created_by=user_id).first()

        if not behavioral_issue:
            abort(404, message="Behavioral issue not found.")

        for key, value in behavioral_issues_data.items():
            setattr(behavioral_issue, key, value)

        try:
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while updating the behavioral issue. {e}")

        return behavioral_issue

    @jwt_required()
    def delete(self, issue_id):
        """Delete a specific behavioral issue by issue ID."""
        user_id = get_jwt_identity()
        behavioral_issue = BIssuesModel.query.filter_by(id=issue_id, created_by=user_id).first()

        if not behavioral_issue:
            abort(404, message="Behavioral issue not found.")

        try:
            db.session.delete(behavioral_issue)
            db.session.commit()
            return {"message": "Behavioral issue deleted."}, 200
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"An error occurred while deleting the behavioral issue. {e}")


@blp.route("/behavioral_issues/participant/<int:participant_id>/month")
class BehavioralIssuesByMonth(MethodView):
    @jwt_required()
    @blp.response(200, BehavioralIssuesResponseSchema(many=True))
    def get(self, participant_id):
        """Get all behavioral issues for a specific participant in the current month."""
        user_id = get_jwt_identity()

        get_participant_or_404(participant_id)

        current_month = datetime.now().month
        current_year = datetime.now().year

        behavioral_issues = BIssuesModel.query.filter(
            and_(
                BIssuesModel.participant_id == participant_id,
                BIssuesModel.created_by == user_id,
                extract('month', BIssuesModel.created_at) == current_month,
                extract('year', BIssuesModel.created_at) == current_year
            )
        ).all()
        return behavioral_issues
