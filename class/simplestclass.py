# -*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'fuhao'
'''
  PROJECT_NAME:python
  PACKAGE_NAME:
  File_Name:simplestclass.py
  User: fuhao
  Date: 13-3-26 : 下午4:43
  descripton:
'''
class Person:
    def __init__(self,name):
        self.name=name
    def sayHI(self):
       print 'hello  ,',self.name

p = Person('pythoner')
p.sayHI()
