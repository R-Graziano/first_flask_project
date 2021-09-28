from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ('Hola Mundo')

@app.route('/new')
def news():
    return ('Bienvenido a un nuevo Mundo')

if __name__ == '__main__':
    app.run(port = 8000, debug = True) #Activar el debug mode permite ver los cambios en tiempo real sin necesidad de volver a ejecutar el archivo