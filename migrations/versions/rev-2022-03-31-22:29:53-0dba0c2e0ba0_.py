"""empty message

Revision ID: 0dba0c2e0ba0
Revises: 760795a6d7eb
Create Date: 2022-03-31 22:29:53.163384

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '0dba0c2e0ba0'
down_revision = '760795a6d7eb'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('public_stream_link', sa.String(), nullable=True))
    op.add_column('events_version', sa.Column('public_stream_link', sa.String(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'public_stream_link')
    op.drop_column('events', 'public_stream_link')
    # ### end Alembic commands ###