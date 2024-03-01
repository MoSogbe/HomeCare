"""empty message

Revision ID: 3e3ab09a9b8e
Revises: 852e72b5e261
Create Date: 2024-02-20 20:50:05.355521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e3ab09a9b8e'
down_revision = '852e72b5e261'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.drop_index('service_charge_duration')
        batch_op.drop_index('service_charge_frequency')
        batch_op.drop_index('service_price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.create_index('service_price', ['service_price'], unique=True)
        batch_op.create_index('service_charge_frequency', ['service_charge_frequency'], unique=True)
        batch_op.create_index('service_charge_duration', ['service_charge_duration'], unique=True)

    # ### end Alembic commands ###
