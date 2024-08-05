"""empty message

Revision ID: 5bb13ea9df93
Revises: 25cfe05f90f3
Create Date: 2024-08-05 15:35:26.039886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bb13ea9df93'
down_revision = '25cfe05f90f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('med_error_reasons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reason', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('med_errors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.Column('mar_id', sa.Integer(), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('error_reason_id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['error_reason_id'], ['med_error_reasons.id'], ),
    sa.ForeignKeyConstraint(['mar_id'], ['prescriptions.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'axis', ['axis_id'], ['id'])

    with op.batch_alter_table('log_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log_entries', schema=None) as batch_op:
        batch_op.drop_column('location')

    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    op.drop_table('med_errors')
    op.drop_table('med_error_reasons')
    # ### end Alembic commands ###
