"""removendo a coluna remove

Revision ID: 8fc423e307ec
Revises: e3f6c652c7a5
Create Date: 2021-09-20 10:47:01.754000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fc423e307ec'
down_revision = 'e3f6c652c7a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tipo', schema=None) as batch_op:
        batch_op.drop_column('remove')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tipo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('remove', sa.VARCHAR(length=20), nullable=True))

    # ### end Alembic commands ###