"""empty message

Revision ID: 3177eb6e81e3
Revises: 3e9a9977aff4
Create Date: 2024-03-22 22:18:08.186277

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3177eb6e81e3'
down_revision = '3e9a9977aff4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participant_service_provider_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_type_id', sa.Integer(), nullable=False),
    sa.Column('provider_name', sa.String(length=55), nullable=False),
    sa.Column('provider_address', sa.String(length=155), nullable=False),
    sa.Column('provider_phone', sa.String(length=155), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['service_type_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_address'),
    sa.UniqueConstraint('provider_name'),
    sa.UniqueConstraint('provider_phone')
    )
    with op.batch_alter_table('participant_service_history', schema=None) as batch_op:
        batch_op.drop_index('provider_address')
        batch_op.drop_index('provider_name')
        batch_op.drop_index('provider_phone')

    op.drop_table('participant_service_history')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participant_service_history',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('service_type_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('provider_name', mysql.VARCHAR(length=55), nullable=False),
    sa.Column('provider_address', mysql.VARCHAR(length=155), nullable=False),
    sa.Column('provider_phone', mysql.VARCHAR(length=155), nullable=False),
    sa.Column('created_by', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('updated_at', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], name='participant_service_history_ibfk_1'),
    sa.ForeignKeyConstraint(['service_type_id'], ['users.id'], name='participant_service_history_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('participant_service_history', schema=None) as batch_op:
        batch_op.create_index('provider_phone', ['provider_phone'], unique=True)
        batch_op.create_index('provider_name', ['provider_name'], unique=True)
        batch_op.create_index('provider_address', ['provider_address'], unique=True)

    op.drop_table('participant_service_provider_history')
    # ### end Alembic commands ###
