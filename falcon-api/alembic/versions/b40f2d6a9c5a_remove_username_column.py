"""remove username column

Revision ID: b40f2d6a9c5a
Revises: 75098ca307c2
Create Date: 2019-09-30 17:53:06.213905

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b40f2d6a9c5a'
down_revision = '75098ca307c2'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('falcon_user', 'username')


def downgrade():
    pass
