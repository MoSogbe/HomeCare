"""empty message

Revision ID: a13cf18aadd3
Revises: 0cdbc42bebfb
Create Date: 2024-03-23 14:37:45.215542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a13cf18aadd3'
down_revision = '0cdbc42bebfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participant_physician',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('physician_address', sa.String(length=155), nullable=False),
    sa.Column('physician_phone', sa.String(length=55), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('physician_address'),
    sa.UniqueConstraint('physician_phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participant_physician')
    # ### end Alembic commands ###
