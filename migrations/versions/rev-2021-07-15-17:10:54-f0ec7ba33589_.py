"""empty message

Revision ID: f0ec7ba33589
Revises: e73500f7f7d9
Create Date: 2021-07-15 17:10:54.948309

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'f0ec7ba33589'
down_revision = 'e73500f7f7d9'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'live_stream_url')
    op.drop_column('events', 'webinar_url')
    op.drop_column('events_version', 'live_stream_url')
    op.drop_column('events_version', 'webinar_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events_version', sa.Column('webinar_url', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('events_version', sa.Column('live_stream_url', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('events', sa.Column('webinar_url', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('events', sa.Column('live_stream_url', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###