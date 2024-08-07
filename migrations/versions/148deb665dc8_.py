"""empty message

Revision ID: 148deb665dc8
Revises: acd4d1a2ea2a
Create Date: 2024-07-09 17:28:21.525865

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '148deb665dc8'
down_revision = 'acd4d1a2ea2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mar_id', sa.Integer(), nullable=False),
    sa.Column('administered_at', sa.DateTime(), nullable=False),
    sa.Column('administered_by', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['mar_id'], ['prescriptions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('log_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('log_entries_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.drop_column('caregiver_id')

    with op.batch_alter_table('prescriptions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('frequency', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('qty', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('todays_frequency', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prescriptions', schema=None) as batch_op:
        batch_op.drop_column('todays_frequency')
        batch_op.drop_column('qty')
        batch_op.drop_column('frequency')

    with op.batch_alter_table('log_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('caregiver_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('log_entries_ibfk_1', 'caregivers', ['caregiver_id'], ['id'])
        batch_op.drop_column('user_id')

    op.drop_table('administrations')
    # ### end Alembic commands ###
