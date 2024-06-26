"""change hashed_password type

Revision ID: 06078d9a1711
Revises: db0944876f9f
Create Date: 2024-06-19 21:45:45.652711

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "06078d9a1711"
down_revision: Union[str, None] = "db0944876f9f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        'ALTER TABLE "user" ALTER COLUMN hashed_password TYPE BYTEA USING hashed_password::bytea'
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "user",
        "hashed_password",
        existing_type=sa.LargeBinary(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
