"""add user table

Revision ID: 127a345dcfec
Revises: b8144cf2e93c
Create Date: 2022-06-17 14:13:30.103998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '127a345dcfec'
down_revision = 'b8144cf2e93c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
            sa.Column('id',sa.Integer(), nullable=False),
            sa.Column('email',sa.String(), nullable=False),
            sa.Column('password',sa.String(), nullable=False),
            sa.Column('created_at',sa.TIMESTAMP('now()'),nullable=False),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('email')
            )

def downgrade() -> None:
    op.drop_table(users)
    pass
