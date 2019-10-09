"""create user and metric table

Revision ID: 5af795a3c5a4
Revises: 
Create Date: 2019-10-09 16:57:27.508457

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5af795a3c5a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # create user table
    op.create_table(
        'user', sa.Column('user_id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(320), unique=True, nullable=False),
        sa.Column('password', sa.String(80), nullable=False),
        sa.Column('token', sa.String(255), nullable=False),
        sa.Column('sid', sa.String(10), nullable=False),
        sa.Column('created',
                  sa.DateTime,
                  server_default=sa.func.current_timestamp()),
        sa.Column('modified',
                  sa.DateTime,
                  server_default=sa.func.current_timestamp()))

    # create metric table
    op.create_table(
        'metric', sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.Integer, nullable=False),
        sa.Column('model_ref', sa.Integer, nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.user_id')),
        sa.Column('created',
                  sa.DateTime,
                  server_default=sa.func.current_timestamp()),
        sa.Column('modified',
                  sa.DateTime,
                  server_default=sa.func.current_timestamp()))


def downgrade():
    # drop user table
    op.drop_table('user')
    # drop metric table
    op.drop_table('user')
