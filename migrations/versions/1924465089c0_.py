"""empty message

Revision ID: 1924465089c0
Revises: 3c34a20bbf8a
Create Date: 2024-06-10 21:40:51.243148

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1924465089c0'
down_revision = '3c34a20bbf8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('daily_notes', schema=None) as batch_op:
        batch_op.alter_column('reviewed_by',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.String(length=11),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('daily_notes', schema=None) as batch_op:
        batch_op.alter_column('reviewed_by',
               existing_type=sa.String(length=11),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=True)

    # ### end Alembic commands ###
