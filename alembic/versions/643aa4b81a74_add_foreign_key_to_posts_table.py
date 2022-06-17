"""add foreign key to posts table

Revision ID: 643aa4b81a74
Revises: 127a345dcfec
Create Date: 2022-06-17 14:23:08.287885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '643aa4b81a74'
down_revision = '127a345dcfec'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table='users',local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
