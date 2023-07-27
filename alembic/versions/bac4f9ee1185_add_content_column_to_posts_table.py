"""add content column to posts table

Revision ID: bac4f9ee1185
Revises: 70ac0c5c06a9
Create Date: 2023-07-26 05:57:03.690219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bac4f9ee1185'
down_revision = '70ac0c5c06a9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
