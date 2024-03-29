"""empty message

Revision ID: 200dd6da580e
Revises: 3fff9a2e9228
Create Date: 2024-03-23 00:00:09.175454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '200dd6da580e'
down_revision = '3fff9a2e9228'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medical_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mi_name', sa.String(length=25), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mi_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medical_information')
    # ### end Alembic commands ###
