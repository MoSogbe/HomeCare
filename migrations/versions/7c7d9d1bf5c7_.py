"""empty message

Revision ID: 7c7d9d1bf5c7
Revises: 12368612a5b1
Create Date: 2024-07-21 12:17:08.228560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c7d9d1bf5c7'
down_revision = '12368612a5b1'
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
