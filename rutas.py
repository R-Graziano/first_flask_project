from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return ('Hola Mundo')

@app.route('/bienvenido')
def welcome_msg():
    return ('Bienvenido a este nuevo Mundo de Flask/Python!')


#localhost:8000/params?params1=Rodrigo_Graziano
#localhost:8000/params
#localhost:8000/params?params1=Rodrigo_Graziano&params2=Anime_Favorito
@app.route('/params')
def params():
    param = request.args.get('params1', ' ...¿no tiene primer parametro?')
    param2 = request.args.get('params2', ' ...¿no tiene un segundo parametro?')
    return 'El parametro es {}, {}'.format(param, param2)

if __name__ == '__main__':
    app.run(port = 8000, debug = True)