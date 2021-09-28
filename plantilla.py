#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ('Hola Mundo')

if __name__ == '__main__':
    app.run(port = 8000, debug = True)