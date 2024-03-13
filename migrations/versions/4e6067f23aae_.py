"""empty message

Revision ID: 4e6067f23aae
Revises: 86fc83b136ac
Create Date: 2024-03-01 23:01:02.403099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e6067f23aae'
down_revision = '86fc83b136ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location_name', sa.String(length=125), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location_name')
    )
    op.create_table('schedule_periods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.String(length=12), nullable=False),
    sa.Column('end_time', sa.String(length=12), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scheduling',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('shift_period_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('caregiver_id', sa.Integer(), nullable=False),
    sa.Column('day_of_week', sa.String(length=10), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('scheduled_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['caregiver_id'], ['caregivers.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['participants.id'], ),
    sa.ForeignKeyConstraint(['scheduled_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['shift_period_id'], ['schedule_periods.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scheduling')
    op.drop_table('schedule_periods')
    op.drop_table('locations')
    # ### end Alembic commands ###
