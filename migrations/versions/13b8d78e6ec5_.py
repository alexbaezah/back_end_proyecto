"""empty message

Revision ID: 13b8d78e6ec5
Revises: 
Create Date: 2022-06-19 23:15:44.295404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13b8d78e6ec5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rut', sa.Integer(), nullable=False),
    sa.Column('dv', sa.String(length=1), nullable=False),
    sa.Column('primer_nombre', sa.String(length=250), nullable=False),
    sa.Column('segundo_nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido_paterno', sa.String(length=250), nullable=False),
    sa.Column('apellido_materno', sa.String(length=250), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=False),
    sa.Column('correo', sa.String(length=250), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rut')
    )
    op.create_table('Comuna',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Descuento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.Column('porcentaje', sa.Float(), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Descuento_Producto',
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('descuento_id', sa.Integer(), nullable=False),
    sa.Column('fecha_inicio', sa.DateTime(), nullable=True),
    sa.Column('fecha_termino', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('producto_id', 'descuento_id')
    )
    op.create_table('Despacho',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('direccion', sa.String(length=250), nullable=False),
    sa.Column('fecha_entrega', sa.DateTime(), nullable=False),
    sa.Column('hora_entrega', sa.DateTime(), nullable=False),
    sa.Column('rut_recibe', sa.String(length=11), nullable=False),
    sa.Column('nombre_recibe', sa.String(length=250), nullable=False),
    sa.Column('estado_despacho', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Detalle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=False),
    sa.Column('descuento', sa.Float(), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Donacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=250), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('valor_venta', sa.Integer(), nullable=False),
    sa.Column('Stock', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=500), nullable=False),
    sa.Column('imagen', sa.String(length=250), nullable=True),
    sa.Column('estado', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Region',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Vendedor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rut', sa.Integer(), nullable=False),
    sa.Column('dv', sa.String(length=1), nullable=False),
    sa.Column('primer_nombre', sa.String(length=250), nullable=False),
    sa.Column('segundo_nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido_paterno', sa.String(length=250), nullable=False),
    sa.Column('apellido_materno', sa.String(length=250), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=False),
    sa.Column('correo', sa.String(length=250), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rut')
    )
    op.create_table('Venta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.Column('descuento', sa.Integer(), nullable=True),
    sa.Column('sub_total', sa.Integer(), nullable=False),
    sa.Column('iva', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('suscripcion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha_inicio', sa.DateTime(), nullable=False),
    sa.Column('fecha_termino', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('suscripcion')
    op.drop_table('Venta')
    op.drop_table('Vendedor')
    op.drop_table('Region')
    op.drop_table('Producto')
    op.drop_table('Donacion')
    op.drop_table('Detalle')
    op.drop_table('Despacho')
    op.drop_table('Descuento_Producto')
    op.drop_table('Descuento')
    op.drop_table('Comuna')
    op.drop_table('Cliente')
    # ### end Alembic commands ###
