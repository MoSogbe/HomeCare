"""empty message

Revision ID: b7f149487c23
Revises: 7f755e0860b9
Create Date: 2024-07-13 10:47:03.195017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7f149487c23'
down_revision = '7f755e0860b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'axis', ['axis_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
