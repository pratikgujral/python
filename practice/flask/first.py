# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 06:14:45 2016

@author: prati
"""

from flask import Flask
app = Flask()

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/greeting/<name>/')
def hello_greeting(name):
    return 'Hello %s' % (name)    

if __name__ == '__main__':
    app.run(debug = True)
