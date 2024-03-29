"""empty message

Revision ID: a620cd3c75f6
Revises: 6455c7ecacaa
Create Date: 2024-03-25 10:41:13.996561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a620cd3c75f6'
down_revision = '6455c7ecacaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diagnosis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medical_condition_id', sa.Integer(), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['medical_condition_id'], ['medical_conditions.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medical_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medical_condition_id', sa.Integer(), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['medical_condition_id'], ['medical_conditions.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medical_information')
    op.drop_table('diagnosis')
    # ### end Alembic commands ###
