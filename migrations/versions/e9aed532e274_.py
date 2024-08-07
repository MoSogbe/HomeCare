"""empty message

Revision ID: e9aed532e274
Revises: add5bc70100c
Create Date: 2024-07-03 10:00:12.227078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9aed532e274'
down_revision = 'add5bc70100c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log_entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('caregiver_id', sa.Integer(), nullable=False),
    sa.Column('check_in', sa.DateTime(), nullable=False),
    sa.Column('check_out', sa.DateTime(), nullable=True),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['caregiver_id'], ['caregivers.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log_entries')
    # ### end Alembic commands ###
