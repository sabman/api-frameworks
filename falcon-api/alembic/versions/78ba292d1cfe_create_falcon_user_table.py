"""create falcon_user table

Revision ID: 78ba292d1cfe
Revises: 
Create Date: 2019-09-26 07:02:57.574888

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '78ba292d1cfe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'falcon_user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('falcon_user')
