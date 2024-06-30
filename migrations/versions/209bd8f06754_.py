"""empty message

Revision ID: 209bd8f06754
Revises: 1924465089c0
Create Date: 2024-06-11 09:13:47.174267

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '209bd8f06754'
down_revision = '1924465089c0'
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