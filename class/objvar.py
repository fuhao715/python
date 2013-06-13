# -*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'fuhao'
'''
  PROJECT_NAME:python
  PACKAGE_NAME:
  File_Name:objvar.py.py
  User: fuhao
  Date: 13-6-13 : 下午5:05
  descripton:
'''


class People:
    population = 0

    def __init__(self, name):
        self.name = name
        self.__class__.population += 1
        print 'name is %s ,population is %d ' % (self.name, self.__class__.population)

    def __del__(self):
        # People.population -= 1
        self.__class__.population -= 1
        if self.__class__.population == 0:
            print 'Population is none '
        else:
            print '%s say bye ,%d' % (self.name, self.__class__.population)

    def sayHi(self):
        print 'hello,%s' % self.name

    def howMany(self):
        print 'how many population %d ' % self.__class__.population


swaroop = People('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = People('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()



