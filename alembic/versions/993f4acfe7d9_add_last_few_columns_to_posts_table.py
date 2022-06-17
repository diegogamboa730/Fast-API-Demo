"""add last few columns to posts table

Revision ID: 993f4acfe7d9
Revises: 643aa4b81a74
Create Date: 2022-06-17 14:35:13.939366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '993f4acfe7d9'
down_revision = '643aa4b81a74'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))

def downgrade() -> None:
    drop_column('posts','published')
    drop_column('posts','created_at')
