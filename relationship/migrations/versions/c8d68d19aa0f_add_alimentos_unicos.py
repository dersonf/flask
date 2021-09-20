"""add alimentos unicos

Revision ID: c8d68d19aa0f
Revises: 113146498352
Create Date: 2021-09-20 10:09:31.559565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8d68d19aa0f'
down_revision = '113146498352'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tipo', schema=None) as batch_op:
        batch_op.create_unique_constraint('foo', ['tipo'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tipo', schema=None) as batch_op:
        batch_op.drop_constraint('foo', type_='unique')

    # ### end Alembic commands ###
