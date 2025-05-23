"""Crear tabla clase

Revision ID: c5b3f519fc00
Revises: b926ce5e52f6
Create Date: 2025-05-16 11:15:12.981394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5b3f519fc00'
down_revision: Union[str, None] = 'b926ce5e52f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clase',
    sa.Column('id_Clase', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=50), nullable=True),
    sa.Column('descripcion', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id_Clase')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clase')
    # ### end Alembic commands ###
