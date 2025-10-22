"""create posts table

Revision ID: a847808e6a13
Revises:
Create Date: 2025-10-22 00:14:25.866623

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a847808e6a13"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("title", sa.String, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
