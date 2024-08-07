"""empty message

Revision ID: 420934d08d99
Revises: 5693b1b95e39
Create Date: 2024-07-12 15:36:00.274561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '420934d08d99'
down_revision = '5693b1b95e39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('axis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('axis_type', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('axis')
    # ### end Alembic commands ###
