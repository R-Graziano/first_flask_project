#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Rodrigo'
    return render_template('base/index2.html', name = name)


@app.route('/client')
def client():
    list_name = ['Test1', 'Test2', 'Test3', 'Test4']
    return render_template('base/client.html', list = list_name)

if __name__ == '__main__':
    app.run(port = 8000, debug = True)