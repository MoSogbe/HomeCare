"""empty message

Revision ID: fb74f51a35bb
Revises: 3e3ab09a9b8e
Create Date: 2024-02-20 20:51:12.185369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb74f51a35bb'
down_revision = '3e3ab09a9b8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location_name', sa.String(length=125), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location_name')
    )
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

    op.drop_table('locations')
    # ### end Alembic commands ###
