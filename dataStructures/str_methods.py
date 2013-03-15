# -*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'fuhao'
'''
  PROJECT_NAME:python
  PACKAGE_NAME:
  File_Name:str_methods.py
  User: fuhao
  Date: 13-3-15 : 下午3:58
  descripton:
'''
name = 'Swaroop' # This is a string object

if name.startswith('Swa'):
    print 'Yes, the string starts with "Swa"'

if 'a' in name:
    print 'Yes, it contains the string "a"'

if name.find('war') != -1:
    print 'Yes, it contains the string "war"'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)
