"""add last few colums to posts table

Revision ID: c876c232916f
Revises: 88506ee0e6e9
Create Date: 2025-10-22 00:46:46.285182

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c876c232916f"
down_revision: Union[str, Sequence[str], None] = "88506ee0e6e9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "created_at")
    op.drop_column("posts", "published")
    pass
