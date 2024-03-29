"""compay info, service category, services

Revision ID: e48bc8dac555
Revises: 15be8d69ae79
Create Date: 2024-01-16 22:00:21.560906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e48bc8dac555'
down_revision = '15be8d69ae79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_of_company', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone_number', sa.String(length=45), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name_of_company'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('service_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=45), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category_name')
    )
    op.create_table('services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_name', sa.String(length=120), nullable=False),
    sa.Column('service_price', sa.String(length=80), nullable=False),
    sa.Column('service_charge_duration', sa.String(length=45), nullable=False),
    sa.Column('service_charge_frequency', sa.String(length=45), nullable=False),
    sa.Column('service_category', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['service_category'], ['service_categories.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('service_charge_duration'),
    sa.UniqueConstraint('service_charge_frequency'),
    sa.UniqueConstraint('service_name'),
    sa.UniqueConstraint('service_price')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('services')
    op.drop_table('service_categories')
    op.drop_table('companies')
    # ### end Alembic commands ###
