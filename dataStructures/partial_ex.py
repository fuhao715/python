# -*- coding: utf-8 -*-
__author__ = 'lenovo'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 14-5-4
 * Time: 下午9:14
 * To change this template use File | Settings | File Templates.
'''
import functools

int2 = functools.partial(int, base=2)

print int2('100000')

print '--------------'

class Student(object):
    pass

s = Student()
s.name = 'michael'
print s.name

def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s, Student)

s.set_age(23)

print s.age

s2 = Student()
# s2.set_age(26) # can't set method to a instance


def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student)

s.set_score(100)
s2.set_score(98)

print s.score, s2.score

print type(set_score)