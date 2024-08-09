"""empty message

Revision ID: d8eae8e86db1
Revises: 50a4c2ca94b3
Create Date: 2024-08-05 16:23:58.698830

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd8eae8e86db1'
down_revision = '50a4c2ca94b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log_entries', schema=None) as batch_op:
        batch_op.drop_column('location')

    with op.batch_alter_table('med_errors', schema=None) as batch_op:
        batch_op.drop_constraint('med_errors_ibfk_3', type_='foreignkey')
        batch_op.drop_constraint('med_errors_ibfk_4', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('med_errors', schema=None) as batch_op:
        batch_op.create_foreign_key('med_errors_ibfk_4', 'prescriptions', ['mar_id'], ['id'])
        batch_op.create_foreign_key('med_errors_ibfk_3', 'participants', ['participant_id'], ['id'])

    with op.batch_alter_table('log_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', mysql.VARCHAR(length=255), nullable=True))

    # ### end Alembic commands ###