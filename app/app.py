from flask import Flask, render_template, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexción MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'flask_prueba'

conexion = MySQL(app)

@app.route('/')
def index():
    # return "¡Hola mundo! Soy Olding"
    cursos = ['PHP', 'Python', 'Java', 'Kotlin', 'Dart', 'JavaScript']
    data={
        'titulo': 'Homepage',
        'bienvenida': 'Cursos disponibles',
        'cursos': cursos,
        'numeros_cursos': len(cursos)
    }
    return render_template('index.html', data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data=data)

@app.route('/cursos')
def listar_cursos():
    data = {}
    try:
        if conexion.connection.open:  # Verificar si la conexión está abierta
            cursor = conexion.connection.cursor()
            sql = "SELECT código, nombre, créditos FROM cursos ORDER BY nombre ASC"
            cursor.execute(sql)
            cursos = cursor.fetchall()
            data['cursos'] = cursos
            data['mensaje'] = 'Exito'
        else:
            data['mensaje'] = 'Conexión a la base de datos cerrada'
    except Exception as ex:
        data['mensaje'] = 'Error =('
        data['detalle_error'] = str(ex)
    return jsonify(data)

def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    ## return redirect(url_for('index'))

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)