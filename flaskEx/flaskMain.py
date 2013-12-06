# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-12-6
# * Time: 下午5:06
# * To change this template use File | Settings | File Templates.
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World Flask 学习'

if __name__ == '__main__':
    app.run()