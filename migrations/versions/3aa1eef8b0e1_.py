"""empty message

Revision ID: 3aa1eef8b0e1
Revises: b14e09a746a3
Create Date: 2024-07-13 22:56:05.251901

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3aa1eef8b0e1'
down_revision = 'b14e09a746a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('participants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address_line_one', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('address_line_two', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('city', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('state', sa.String(length=100), nullable=False))
        batch_op.drop_column('home_address')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('participants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('home_address', mysql.VARCHAR(length=100), nullable=True))
        batch_op.drop_column('state')
        batch_op.drop_column('city')
        batch_op.drop_column('address_line_two')
        batch_op.drop_column('address_line_one')

    # ### end Alembic commands ###
