# 0. ejecutamos pip install flask flask-sqlalchemy flask-migrate flask-cors
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Region(db.Model):
    __tablename__ ='Region'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250), nullable = False)


class Comuna(db.Model):
    __tablename__ = 'Comuna'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250), nullable = False)
    # region_id = db.Column(db.Integer, nullable = False) 
    

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    id = db.Column(db.Integer, primary_key = True)
    rut = db.Column(db.Integer, unique = True, nullable = False)
    dv = db.Column(db.String(1), nullable = False)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)
    telefono = db.Column(db.Integer, nullable = False)
    correo = db.Column(db.String(250), nullable = False)
    estado = db.Column(db.Integer, nullable= False)
    # comuna_id = db.Column(db.Integer, nullable = False) 

class Vendedor(db.Model):
    __tablename__ = 'Vendedor'
    id = db.Column(db.Integer, primary_key = True)
    rut = db.Column(db.Integer, unique = True, nullable = False)
    dv = db.Column(db.String(1), nullable = False)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)
    telefono = db.Column(db.Integer, nullable = False)
    correo = db.Column(db.String(250), nullable = False)
    estado = db.Column(db.Integer, nullable= False)
    # comuna_id = db.Column(db.Integer, nullable = False) 


class Despacho(db.Model):
    __tablename__ = 'Despacho'
    id = db.Column(db.Integer, primary_key = True)
    direccion = db.Column(db.String(250), nullable = False)
    fecha_entrega = db.Column(db.DateTime, nullable = False)
    hora_entrega = db.Column(db.DateTime, nullable = False)
    rut_recibe = db.Column(db.String(11), nullable = False)
    nombre_recibe = db.Column(db.String(250), nullable = False)
    estado_despacho = db.Column(db.Boolean, nullable = False, default = False)
    
class Descuento(db.Model):
    __tablename__ = 'Descuento'
    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(250), nullable = False)
    fecha = db.Column(db.DateTime, nullable = False)
    porcentaje = db.Column(db.Float, nullable = False)
    estado = db.Column(db.Integer, nullable = False)
    
class Descuento_Producto(db.Model):
    __tablename__ = 'Descuento_Producto'
    producto_id = db.Column(db.Integer, primary_key = True)
    descuento_id = db.Column(db.Integer, primary_key = True)
    fecha_inicio = db.Column(db.DateTime, nullable = True)
    fecha_termino = db.Column(db.DateTime, nullable = True)

class Producto(db.Model):
    __tablename__= 'Producto'
    id = db.Column(db.Intenger, primary_key = True)
    codigo = db.Column(db.String(250), nullable = False)
    nombre = db.Column(db.String(250), nullable = False)
    valor_venta = db.Column(db.Integer, nullable = False)
    Stock = db.Column(db.Integer, nullable = False)
    descripcion = db.Column(db.String(500), nullable = False)
    imagen = db.Column(db.String(250), nullable = True)
    estado = db.Column(db.Integer, nullable = True )

class Suscripcion(db.Model):
    __tablaname__ = 'Suscripcion'
    id = db.Column(db.Intenger, primary_key = True)
    fecha_inicio = db.Column(db.DateTime, nullable = False)
    fecha_termino = db.Column(db.DateTime, nullable = True)
    # cliente_id = db.Column(db.Integer, nullable = False) 
        
class Donacion(db.Model):
    __tablename__ = 'Donacion'
    id = db.Column(db.Intenger, primary_key = True)
    valor = db.Column(db.Integer, nullable = False)
    fecha = db.Column(db.DateTime, nullable = False)
    # cliente_id = db.Column(db.Integer, nullable = False) 

class Detalle(db.Model):
    __tablename__ = 'Detalle'
    id = db.Column(db.Integer, primary_key = True)
    cantidad = db.Column(db.Integer, nullable = False)
    valor = db.Column(db.Integer, nullable = False)
    descuento = db.Column(db.Float, nullable = True)
    estado = db.Column(db.Integer, nullable = False )
    # venta_id = db.Column(db.Integer, nullable = False) 
    # producto_id = db.Column(db.Integer, nullable = False)
    
    

class Venta(db.Model):
    __tablename__ = 'Venta'
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, nullable = False)
    descuento = db.Column(db.Integer, nullable = True)
    sub_total = db.Column(db.Integer, nullable = False)
    iva = db.Column(db.Integer, nullable = False)
    total = db.Column(db.Integer, nullable = False )
    estado = db.Column(db.Integer, nullable = False)
    # cliente_id = db.Column(db.Integer, nullable = False) 
    # vendedor_id = db.Column(db.Integer, nullable = False) 
    # despacho_id = db.Column(db.Integer, nullable = False) 





    





