# coding=utf-8
"""refs year_int 9999

Revision ID: 4256d27f1cde
Revises: 487d9c6b4866
Create Date: 2014-10-21 12:17:38.533000

"""

# revision identifiers, used by Alembic.

revision = '4256d27f1cde'
down_revision = '487d9c6b4866'

import datetime

from alembic import op
import sqlalchemy as sa


def upgrade():
    update_source = sa.text("UPDATE source SET updated = now(), "
        "year_int = reverse(substring(reverse(year) from '(?:^|\D)(\d{4})(?!\d)'))::int "
        "WHERE year_int > 3000 OR year_int < 10")
    op.execute(update_source)


def downgrade():
    pass
