"""empty message

Revision ID: d6a692fcb2b3
Revises: dee7c23a4532
Create Date: 2021-02-14 20:58:32.684020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6a692fcb2b3'
down_revision = 'dee7c23a4532'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('max_total', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'max_total')
    # ### end Alembic commands ###