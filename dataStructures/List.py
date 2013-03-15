# -*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'fuhao'
'''
  PROJECT_NAME:python
  PACKAGE_NAME:
  File_Name:List.py
  User: fuhao
  Date: 13-3-15 : 上午10:22
  descripton:
'''
fruitList = ['apple','orange','mango','banana']
print 'the length of the fruitList = ',len(fruitList)
print fruitList
print 'the first fruit is ',fruitList[0]
for fruit in fruitList:
    print fruit,
print '\nI also have to buy rice.'
del fruitList[0]
print fruitList
fruitList.append('carrot')
print fruitList
fruitList.sort()


