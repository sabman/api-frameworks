"""Add metric_value & model_id columns

Revision ID: 75098ca307c2
Revises: 78ba292d1cfe
Create Date: 2019-09-30 14:51:46.156612

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '75098ca307c2'
down_revision = '78ba292d1cfe'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('falcon_user', sa.Column('metric_value', sa.String(50)))
    op.add_column('falcon_user', sa.Column('model_id', sa.String(50)))


def downgrade():
    op.drop_column('falcon_user', 'metric_value')
    op.drop_column('falcon_user', 'model_id')
