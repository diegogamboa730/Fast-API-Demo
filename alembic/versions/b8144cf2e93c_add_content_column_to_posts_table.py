"""add content column to posts table

Revision ID: b8144cf2e93c
Revises: 844eb1ee4245
Create Date: 2022-06-17 13:56:22.162332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8144cf2e93c'
down_revision = '844eb1ee4245'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))    

def downgrade() -> None:
    op.drop_column('posts','content')
