"""empty message

Revision ID: 687034af0ed7
Revises: 420934d08d99
Create Date: 2024-07-12 16:30:13.933213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '687034af0ed7'
down_revision = '420934d08d99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.add_column(sa.Column('axis_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'axis', ['axis_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('axis_id')

    # ### end Alembic commands ###
