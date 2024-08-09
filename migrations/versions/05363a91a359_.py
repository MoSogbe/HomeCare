"""empty message

Revision ID: 05363a91a359
Revises: a6be31217949
Create Date: 2024-07-14 09:18:39.250219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05363a91a359'
down_revision = 'a6be31217949'
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