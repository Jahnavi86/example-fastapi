"""create posts table

Revision ID: 70ac0c5c06a9
Revises: 
Create Date: 2023-07-26 05:26:12.243630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70ac0c5c06a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():#handles changes
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():#reverses to original i.e undo changes
    op.drop_table('posts')
    pass
