"""empty message

Revision ID: 5232793c6b81
Revises: 4e6067f23aae
Create Date: 2024-03-22 22:00:01.815695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5232793c6b81'
down_revision = '4e6067f23aae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participant_service_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_type_id', sa.Integer(), nullable=False),
    sa.Column('provider_name', sa.String(length=55), nullable=False),
    sa.Column('provider_address', sa.String(length=155), nullable=False),
    sa.Column('provider_phone', sa.String(length=155), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_address'),
    sa.UniqueConstraint('provider_name'),
    sa.UniqueConstraint('provider_phone'),
    sa.UniqueConstraint('service_type_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participant_service_history')
    # ### end Alembic commands ###
