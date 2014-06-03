# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 2014/6/3
 * Time: 21:17
 * To change this template use File | Settings | File Templates.
'''
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()