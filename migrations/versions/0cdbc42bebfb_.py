"""empty message

Revision ID: 0cdbc42bebfb
Revises: 06ee11d23552
Create Date: 2024-03-23 12:35:30.094261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cdbc42bebfb'
down_revision = '06ee11d23552'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('preferred_hospital',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ph_name', sa.String(length=55), nullable=False),
    sa.Column('ph_address', sa.String(length=155), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ph_address'),
    sa.UniqueConstraint('ph_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('preferred_hospital')
    # ### end Alembic commands ###
