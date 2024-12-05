from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)