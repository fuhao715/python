# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-10-23
# * Time: 下午3:56
# * To change this template use File | Settings | File Templates.

from soaplib.service import rpc
from soaplib.service import DefinitionBase
from soaplib.serializers.primitive import String, Integer

from soaplib.wsgi import Application
from soaplib.serializers.clazz import Array


class HelloWorldService(DefinitionBase):
    @rpc(String, Integer, _returns=Array(String))
    def say_hello(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s' % name)
        return results

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        server = make_server('localhost', 7789, Application([HelloWorldService], 'tns'))
        server.serve_forever()
    except ImportError:
        print "Error: example server code requires Python >= 2.5"