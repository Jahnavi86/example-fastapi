"""add foreaign-key to posts table

Revision ID: 54629be476b6
Revises: 7ada2b2bf000
Create Date: 2023-07-26 06:17:37.503328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54629be476b6'
down_revision = '7ada2b2bf000'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
