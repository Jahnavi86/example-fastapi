"""add phone number

Revision ID: 7967de8792dc
Revises: 1df71af38548
Create Date: 2023-07-26 07:20:41.248991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7967de8792dc'
down_revision = '1df71af38548'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
