# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-10-23
# * Time: 下午4:45
# * To change this template use File | Settings | File Templates.
from suds.client import Client
hello_client = Client('http://localhost:7789/?wsdl')
result = hello_client.service.say_hello("Dave", 5)
print result