"""add foriegn key

Revision ID: 511207448317
Revises: c07239cf5e80
Create Date: 2021-11-30 12:33:51.547740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '511207448317'
down_revision = 'c07239cf5e80'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'owner_id', sa.Integer(),  	nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", 	referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], 	ondelete="CASCADE")

    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
