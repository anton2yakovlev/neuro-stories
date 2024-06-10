"""update user table

Revision ID: 951e791e82b6
Revises: a2c7221d848c
Create Date: 2024-06-01 00:05:14.049584

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "951e791e82b6"
down_revision: Union[str, None] = "a2c7221d848c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("hashed_password", sa.String(), nullable=True))
    op.alter_column("user", "active_user", existing_type=sa.BOOLEAN(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("user", "active_user", existing_type=sa.BOOLEAN(), nullable=False)
    op.drop_column("user", "hashed_password")
    # ### end Alembic commands ###