"""empty message

Revision ID: ea3218f68ba6
Revises: efc7959d2a48
Create Date: 2024-06-09 22:04:23.576275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea3218f68ba6'
down_revision = 'efc7959d2a48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('daily_notes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reviewed_by', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['reviewed_by'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('daily_notes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('reviewed_by')

    # ### end Alembic commands ###
