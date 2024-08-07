"""empty message

Revision ID: 9f14ff08a8a3
Revises: 7c7d9d1bf5c7
Create Date: 2024-07-28 11:38:56.286105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f14ff08a8a3'
down_revision = '7c7d9d1bf5c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrative_documentations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('document_type_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('file_path', sa.String(length=255), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['document_type_id'], ['document_types.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('administrative_documentations')
    # ### end Alembic commands ###
