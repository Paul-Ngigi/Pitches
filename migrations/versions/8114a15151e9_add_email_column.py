"""add email column

Revision ID: 8114a15151e9
Revises: af8c0e69d359
Create Date: 2021-04-25 12:41:17.425734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8114a15151e9'
down_revision = 'af8c0e69d359'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###