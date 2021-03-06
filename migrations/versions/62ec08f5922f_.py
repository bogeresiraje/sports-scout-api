"""empty message

Revision ID: 62ec08f5922f
Revises: a87e4d75daeb
Create Date: 2019-05-29 23:31:17.226335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62ec08f5922f'
down_revision = 'a87e4d75daeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('manager', sa.Column('first_name', sa.String(length=100), nullable=False))
    op.add_column('manager', sa.Column('last_name', sa.String(length=100), nullable=False))
    op.drop_constraint('manager_username_key', 'manager', type_='unique')
    op.drop_column('manager', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('manager', sa.Column('username', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.create_unique_constraint('manager_username_key', 'manager', ['username'])
    op.drop_column('manager', 'last_name')
    op.drop_column('manager', 'first_name')
    # ### end Alembic commands ###
