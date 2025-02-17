"""rename department

Revision ID: 80597db6d029
Revises: b7f427027300
Create Date: 2024-01-08 15:47:58.167707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80597db6d029'
down_revision = 'b7f427027300'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
