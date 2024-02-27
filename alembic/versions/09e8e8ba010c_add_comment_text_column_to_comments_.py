"""Add comment_text column to comments table

Revision ID: 09e8e8ba010c
Revises: 
Create Date: 2024-02-26 16:15:13.483160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09e8e8ba010c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add the comment_text column to the comments table
    op.add_column('comments', sa.Column('comment_text', sa.String(length=255), nullable=True))


def downgrade() -> None:
    # Remove the comment_text column from the comments table
    op.drop_column('comments', 'comment_text')
