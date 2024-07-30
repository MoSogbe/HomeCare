"""empty message

Revision ID: 540c555780f3
Revises: 849e8d9d9c79
Create Date: 2024-07-30 09:13:09.279145

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '540c555780f3'
down_revision = '849e8d9d9c79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('administrative_documentations', schema=None) as batch_op:
        batch_op.drop_constraint('administrative_documentations_ibfk_3', type_='foreignkey')
        batch_op.drop_column('participant_id')

    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'axis', ['axis_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('administrative_documentations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('participant_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('administrative_documentations_ibfk_3', 'participants', ['participant_id'], ['id'])

    # ### end Alembic commands ###
