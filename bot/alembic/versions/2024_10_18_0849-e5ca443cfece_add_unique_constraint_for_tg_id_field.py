"""add unique constraint for tg_id field

Revision ID: e5ca443cfece
Revises: 0ce6492296d1
Create Date: 2024-10-18 08:49:58.128534

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e5ca443cfece"
down_revision: Union[str, None] = "0ce6492296d1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(op.f("uq_users_tg_id"), "users", ["tg_id"])


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_tg_id"), "users", type_="unique")
