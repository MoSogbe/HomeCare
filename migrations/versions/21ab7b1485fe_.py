"""empty message

Revision ID: 21ab7b1485fe
Revises: 788edb4b1e9d
Create Date: 2024-03-23 12:14:20.274517

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '21ab7b1485fe'
down_revision = '788edb4b1e9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('case_manager', schema=None) as batch_op:
        batch_op.alter_column('cm_fax',
               existing_type=mysql.VARCHAR(length=225),
               type_=sa.String(length=45),
               existing_nullable=True)
        batch_op.alter_column('cm_email_address',
               existing_type=mysql.VARCHAR(length=225),
               type_=sa.String(length=125),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('case_manager', schema=None) as batch_op:
        batch_op.alter_column('cm_email_address',
               existing_type=sa.String(length=125),
               type_=mysql.VARCHAR(length=225),
               existing_nullable=True)
        batch_op.alter_column('cm_fax',
               existing_type=sa.String(length=45),
               type_=mysql.VARCHAR(length=225),
               existing_nullable=True)

    # ### end Alembic commands ###
