"""empty message

Revision ID: fc19fd0db20a
Revises: 50bfedba2bef
Create Date: 2024-03-24 14:07:00.817631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc19fd0db20a'
down_revision = '50bfedba2bef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('case_manager',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cm_name', sa.String(length=55), nullable=False),
    sa.Column('cm_phone', sa.String(length=55), nullable=False),
    sa.Column('cm_emergency_phone', sa.String(length=55), nullable=True),
    sa.Column('cm_address', sa.String(length=225), nullable=False),
    sa.Column('cm_fax', sa.String(length=45), nullable=True),
    sa.Column('cm_email_address', sa.String(length=125), nullable=True),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cm_address'),
    sa.UniqueConstraint('cm_email_address'),
    sa.UniqueConstraint('cm_emergency_phone'),
    sa.UniqueConstraint('cm_fax'),
    sa.UniqueConstraint('cm_name'),
    sa.UniqueConstraint('cm_phone')
    )
    op.create_table('eci',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gaurdian_name', sa.String(length=55), nullable=False),
    sa.Column('gaurdian_phone', sa.String(length=55), nullable=False),
    sa.Column('gaurdian_address', sa.String(length=225), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('gaurdian_address'),
    sa.UniqueConstraint('gaurdian_name'),
    sa.UniqueConstraint('gaurdian_phone')
    )
    op.create_table('participant_physician',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('physician_name', sa.String(length=55), nullable=False),
    sa.Column('physician_phone', sa.String(length=55), nullable=False),
    sa.Column('physician_address', sa.String(length=155), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('physician_address'),
    sa.UniqueConstraint('physician_name'),
    sa.UniqueConstraint('physician_phone')
    )
    op.create_table('preferred_hospital',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ph_name', sa.String(length=55), nullable=False),
    sa.Column('ph_address', sa.String(length=155), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['participant_id'], ['participants.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ph_address'),
    sa.UniqueConstraint('ph_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('preferred_hospital')
    op.drop_table('participant_physician')
    op.drop_table('eci')
    op.drop_table('case_manager')
    # ### end Alembic commands ###
