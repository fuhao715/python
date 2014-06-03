# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 2014/6/3
 * Time: 18:31
 * To change this template use File | Settings | File Templates.
'''
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('localhost', 8000, application)
print 'Serving HTTP on port 8000'

# 开始监听HTTP请求:
httpd.serve_forever()
