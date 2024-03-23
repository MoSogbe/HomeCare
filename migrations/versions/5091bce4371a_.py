"""empty message

Revision ID: 5091bce4371a
Revises: 8d0745bf77d8
Create Date: 2024-03-22 23:23:06.146426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5091bce4371a'
down_revision = '8d0745bf77d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diagnosis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('axis', sa.String(length=12), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('axis')
    )
    op.create_table('participant_service_provider_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('service_type_id', sa.Integer(), nullable=False),
    sa.Column('provider_name', sa.String(length=55), nullable=False),
    sa.Column('provider_address', sa.String(length=155), nullable=False),
    sa.Column('provider_phone', sa.String(length=155), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.ForeignKeyConstraint(['service_type_id'], ['services.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_address'),
    sa.UniqueConstraint('provider_name'),
    sa.UniqueConstraint('provider_phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participant_service_provider_history')
    op.drop_table('diagnosis')
    # ### end Alembic commands ###
