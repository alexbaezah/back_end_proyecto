# 0. ejecutamos pip install flask flask-sqlalchemy flask-migrate flask-cors
# 1. importamos la libreria flask
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Cliente
from flask_cors import CORS, cross_origin

# 2. Creamos la aplicacion
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

# 6. Creamos una ruta para validar nuestra app
@app.route('/')
def index():
    return 'Hola mundo'

    # Consultar todos
@app.route('/clientes', methods=['GET'])
def getClientes():
    cliente = Cliente.query.all()
    cliente = list(map(lambda x: x.serialize(), cliente))
    return jsonify(cliente),200

# consulta solo un usuario según su id y me devuelve 1
@app.route('/clientes/<id>', methods=['GET'])
def getCliente(id):
    cliente = Cliente.query.get('id')
    return jsonify(cliente.serialize()),200

# borrar usuario segun id
@app.route('/clientes/<id>', methods=['DELETE'])
def deleteCliente(id):
    cliente = Cliente.query.get('id')
    Cliente.delete(cliente)
    return jsonify(cliente.serialize()),200

# modificar usuario
@app.route('/clientes/<id>', methods=['PUT'])
def updateCliente(id):
    cliente = Cliente.query.get('id')

    rut = request.json.get('rut')
    dv = request.json.get('dv')
    primer_nombre = request.json.get('primer_nombre')
    segundo_nombre = request.json.get('segundo_nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    direccion = request.json.get('direccion')
    telefono = request.json.get('telefono')
    correo = request.json.get('correo')
    estado = request.json.get('estado')

    cliente.rut = rut
    cliente.dv = dv
    cliente.primer_nombre = primer_nombre
    cliente.segundo_nombre = segundo_nombre
    cliente.apellido_paterno = apellido_paterno
    cliente.apellido_materno = apellido_materno
    cliente.direccion = direccion
    cliente.telefono = telefono 
    cliente.correo = correo
    cliente.estado = estado
    Cliente.save(cliente)

    return jsonify(cliente.serialize()),200

# agregar usuario
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/clientes', methods=['POST'])
def addCliente():
    cliente = Cliente()
    rut = request.json.get('rut')
    dv = request.json.get('dv')
    primer_nombre = request.json.get('primer_nombre')
    segundo_nombre = request.json.get('segundo_nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    direccion = request.json.get('direccion')
    telefono = request.json.get('telefono')
    correo = request.json.get('correo')
    estado = request.json.get('estado')

    cliente.rut = rut 
    cliente.dv = dv
    cliente.primer_nombre = primer_nombre
    cliente.segundo_nombre = segundo_nombre
    cliente.apellido_paterno = apellido_paterno
    cliente.apellido_materno = apellido_materno
    cliente.direccion = direccion
    cliente.telefono = telefono 
    cliente.correo = correo
    cliente.estado = estado
    Cliente.save(cliente)


    return jsonify(cliente.serialize()),200


# 3. Creamos una ruta y debug=true para que el servidor se reinicie ante los cambios
# 4. añadimos un validador para saber si estamos ejecutando nuestra aplicacion
# 5. ejecutamos python app.py o python3 app.py
# 6. ejecutamos el comando flask db init
# 7. ejecutamos el comando flask db migrate
# 8. ejecutamos el comando flask db upgrade
# 9. ejecutamos el comando flask run --host=0.0.0.0 en caso que tengamos problemas con el cors
if __name__ == '__main__':
    app.run(port=3000, debug=True)