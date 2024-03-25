"""empty message

Revision ID: 82dd36c4f59d
Revises: 85b3f875b14a
Create Date: 2024-03-25 02:56:41.191731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82dd36c4f59d'
down_revision = '85b3f875b14a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('batch_num_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('batch_num', sa.String(length=125), nullable=False),
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('transaction_code', sa.String(length=125), nullable=False),
    sa.Column('batch_code', sa.String(length=125), nullable=False),
    sa.Column('quatity_received', sa.String(length=12), nullable=False),
    sa.Column('expiry_date', sa.DateTime(), nullable=False),
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock_total',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total_qty', sa.String(length=125), nullable=False),
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock_total')
    op.drop_table('stock')
    op.drop_table('batch_num_records')
    # ### end Alembic commands ###
