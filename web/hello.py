# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 2014/6/3
 * Time: 18:30
 * To change this template use File | Settings | File Templates.
'''
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello %s </h1>' % (environ['PATH_INFO'][1:] or 'web')

