from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return ('Hola Mundo')

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name ='undefined', num = 'undefined'):
    return 'El parametro es {} {}'.format(name, num)

if __name__ == '__main__':
    app.run(port = 8000, debug = True)