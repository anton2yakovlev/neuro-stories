"""empty message

Revision ID: a2c7221d848c
Revises: 4b97d48e9cfa
Create Date: 2024-06-01 00:04:21.094338

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a2c7221d848c"
down_revision: Union[str, None] = "4b97d48e9cfa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
