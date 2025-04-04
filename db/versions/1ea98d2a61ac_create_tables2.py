"""create tables2

Revision ID: 1ea98d2a61ac
Revises: aec8b9a3321a
Create Date: 2025-01-14 22:16:57.641099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1ea98d2a61ac'
down_revision: Union[str, None] = 'aec8b9a3321a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # op.drop_table('todos')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('detail', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('deadline', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('create_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='todos_pkey')
    )
    op.create_table('users',
    sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('user_email', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='users_pkey')
    )
    # ### end Alembic commands ###
