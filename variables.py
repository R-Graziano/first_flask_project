#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/')
@app.route('/user/<name>')
def user(name='Rodrigo'):
    age = 23
    my_list = [1,2,3,4]
    return render_template('user.html', nombre = name, edad = age, lista = my_list)

if __name__ == '__main__':
    app.run(port = 8000, debug = True)