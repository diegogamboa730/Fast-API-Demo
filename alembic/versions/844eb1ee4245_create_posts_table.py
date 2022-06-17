"""create posts table

Revision ID: 844eb1ee4245
Revises: 
Create Date: 2022-06-17 13:38:51.667695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '844eb1ee4245'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title',sa.String(), nullable=False))
    
def downgrade() -> None:
    op.drop_table('posts')
