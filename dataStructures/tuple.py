# -*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'fuhao'
'''
  PROJECT_NAME:python
  PACKAGE_NAME:
  File_Name:tuple.py
  User: fuhao
  Date: 13-3-15 : 上午10:45
  descripton:
'''
zoo = ('wolf', 'elephant', 'penguin')
print "zoo's length : ",len(zoo),'zoo is ',zoo
new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print 'All animals in new zoo are', new_zoo
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animal brought from old zoo is', new_zoo[2][2]

zero = ()
one = ('one12',)
print one
age = 22
name = 'Swaroop'

print '%s is %d years old' % (name, age)
print 'Why is %s playing with that python?' % name
