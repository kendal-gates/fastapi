"""add content column to post table

Revision ID: 2e56a2ff421d
Revises: 25b0827164a5
Create Date: 2021-11-30 12:30:49.315820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e56a2ff421d'
down_revision = '25b0827164a5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
