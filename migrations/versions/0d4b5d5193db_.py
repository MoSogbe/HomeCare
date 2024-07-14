"""empty message

Revision ID: 0d4b5d5193db
Revises: c047fdea2c25
Create Date: 2024-07-13 22:51:38.764803

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0d4b5d5193db'
down_revision = 'c047fdea2c25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log_entries', schema=None) as batch_op:
        batch_op.alter_column('check_out',
               existing_type=mysql.DATETIME(),
               type_=sa.String(length=255),
               existing_nullable=True)

    with op.batch_alter_table('participants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address_line_one', sa.String(length=255), nullable=True))
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
        batch_op.drop_column('address_line_one')

    with op.batch_alter_table('log_entries', schema=None) as batch_op:
        batch_op.alter_column('check_out',
               existing_type=sa.String(length=255),
               type_=mysql.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
