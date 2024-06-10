"""empty message

Revision ID: 16bc06fdb6f1
Revises: 04ecde3d76e7
Create Date: 2024-06-08 11:02:40.658667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16bc06fdb6f1'
down_revision = '04ecde3d76e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prescriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.Column('reason_for_medication', sa.String(length=145), nullable=False),
    sa.Column('mar_date', sa.String(length=24), nullable=False),
    sa.Column('mar_time', sa.String(length=24), nullable=False),
    sa.Column('place_of_mar', sa.String(length=125), nullable=True),
    sa.Column('dossage', sa.String(length=125), nullable=False),
    sa.Column('comment', sa.String(length=225), nullable=True),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vitals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blood_pressure', sa.String(length=24), nullable=True),
    sa.Column('systolic', sa.String(length=24), nullable=True),
    sa.Column('diastolic', sa.String(length=145), nullable=True),
    sa.Column('pulse', sa.String(length=24), nullable=True),
    sa.Column('glucose', sa.String(length=24), nullable=True),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=225), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vitals')
    op.drop_table('prescriptions')
    # ### end Alembic commands ###
