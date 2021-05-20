"""empty message

Revision ID: 21e59676e268
Revises: d0ff834a357e
Create Date: 2021-05-19 18:31:12.468509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21e59676e268'
down_revision = 'd0ff834a357e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rentals', sa.Column('due_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rentals', 'due_date')
    # ### end Alembic commands ###
