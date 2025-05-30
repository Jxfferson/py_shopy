"""tablas de bd para proyecto

Revision ID: 84536054a867
Revises: 
Create Date: 2025-05-26 11:03:53.769530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84536054a867'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Rol',
    sa.Column('id_Rol', sa.Integer(), nullable=False),
    sa.Column('nombre_Rol', sa.String(length=50), nullable=True),
    sa.Column('estado_Rol', sa.Boolean(), nullable=True),
    sa.Column('descripcion_Rol', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id_Rol')
    )
    op.create_table('categoria_habilidad',
    sa.Column('id_categoria', sa.Integer(), nullable=False),
    sa.Column('categoria', sa.String(length=200), nullable=True),
    sa.Column('descripcion', sa.String(length=200), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id_categoria')
    )
    op.create_table('usuario',
    sa.Column('id_Usuario', sa.Integer(), nullable=False),
    sa.Column('nombre_Usuario', sa.String(length=50), nullable=True),
    sa.Column('apellido_Usuario', sa.String(length=50), nullable=True),
    sa.Column('email_Usuario', sa.String(length=60), nullable=True),
    sa.Column('password_Usuario', sa.String(length=100), nullable=True),
    sa.Column('fecha_Creacion', sa.Date(), nullable=True),
    sa.Column('trueques_Usuario', sa.Integer(), nullable=True),
    sa.Column('fecha_registro', sa.Date(), nullable=True),
    sa.Column('foto_perfil', sa.String(length=255), nullable=True),
    sa.Column('descripcion_Usuario', sa.String(length=200), nullable=True),
    sa.Column('rol_UsuarioFK', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rol_UsuarioFK'], ['Rol.id_Rol'], ),
    sa.PrimaryKeyConstraint('id_Usuario')
    )
    op.create_table('habilidades',
    sa.Column('id_Habilidades', sa.Integer(), nullable=False),
    sa.Column('nombre_Habilidades', sa.String(length=50), nullable=True),
    sa.Column('descripcion_Habilidades', sa.String(length=200), nullable=True),
    sa.Column('categoria_Habilidades', sa.String(length=50), nullable=True),
    sa.Column('id_usuarioFK', sa.Integer(), nullable=True),
    sa.Column('categoria_Habilidad', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoria_Habilidad'], ['categoria_habilidad.id_categoria'], ),
    sa.ForeignKeyConstraint(['id_usuarioFK'], ['usuario.id_Usuario'], ),
    sa.PrimaryKeyConstraint('id_Habilidades')
    )
    op.create_table('curso',
    sa.Column('id_Curso', sa.Integer(), nullable=False),
    sa.Column('nombre_Curso', sa.String(length=50), nullable=True),
    sa.Column('descripcion_Curso', sa.String(length=200), nullable=True),
    sa.Column('fecha_Curso', sa.Date(), nullable=True),
    sa.Column('estado_Curso', sa.Boolean(), nullable=True),
    sa.Column('calificaciones', sa.Float(), nullable=True),
    sa.Column('id_UsuarioFK', sa.Integer(), nullable=True),
    sa.Column('id_HabilidadesFK', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_HabilidadesFK'], ['habilidades.id_Habilidades'], ),
    sa.ForeignKeyConstraint(['id_UsuarioFK'], ['usuario.id_Usuario'], ),
    sa.PrimaryKeyConstraint('id_Curso')
    )
    op.create_table('intercambios',
    sa.Column('id_Intercambios', sa.Integer(), nullable=False),
    sa.Column('fecha_Intercambio', sa.Date(), nullable=True),
    sa.Column('estado_Intercambio', sa.Boolean(), nullable=True),
    sa.Column('descripcion_Intercambio', sa.String(length=200), nullable=True),
    sa.Column('id_UsuarioFK', sa.Integer(), nullable=True),
    sa.Column('id_HabilidadesFK', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_HabilidadesFK'], ['habilidades.id_Habilidades'], ),
    sa.ForeignKeyConstraint(['id_UsuarioFK'], ['usuario.id_Usuario'], ),
    sa.PrimaryKeyConstraint('id_Intercambios')
    )
    op.create_table('materiales',
    sa.Column('id_Materiales', sa.Integer(), nullable=False),
    sa.Column('nombre_Materiales', sa.String(length=50), nullable=True),
    sa.Column('descripcion_Materiales', sa.String(length=200), nullable=True),
    sa.Column('tipo_Materiales', sa.Enum('documento', 'video', 'audio'), nullable=True),
    sa.Column('url_Materiales', sa.String(length=200), nullable=True),
    sa.Column('fecha_Subida', sa.Date(), nullable=True),
    sa.Column('id_IntercambioFK', sa.Integer(), nullable=True),
    sa.Column('id_cursoFK', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_IntercambioFK'], ['intercambios.id_Intercambios'], ),
    sa.ForeignKeyConstraint(['id_cursoFK'], ['curso.id_Curso'], ),
    sa.PrimaryKeyConstraint('id_Materiales')
    )
    op.create_table('sesiones',
    sa.Column('id_sesiones', sa.Integer(), nullable=False),
    sa.Column('fecha_inicio', sa.Date(), nullable=True),
    sa.Column('hora_inicio', sa.Time(), nullable=True),
    sa.Column('tematica', sa.String(length=200), nullable=True),
    sa.Column('Estado', sa.Boolean(), nullable=True),
    sa.Column('id_IntercambioFK', sa.Integer(), nullable=True),
    sa.Column('id_cursoFK', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_IntercambioFK'], ['intercambios.id_Intercambios'], ),
    sa.ForeignKeyConstraint(['id_cursoFK'], ['curso.id_Curso'], ),
    sa.PrimaryKeyConstraint('id_sesiones')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sesiones')
    op.drop_table('materiales')
    op.drop_table('intercambios')
    op.drop_table('curso')
    op.drop_table('habilidades')
    op.drop_table('usuario')
    op.drop_table('categoria_habilidad')
    op.drop_table('Rol')
    # ### end Alembic commands ###
