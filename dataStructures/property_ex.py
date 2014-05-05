# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 14-5-5
 * Time: 下午3:32
 * To change this template use File | Settings | File Templates.
'''
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
         if not isinstance(value, int):
             raise ValueError('score must be an Integer')
         elif value < 0 or value >100:
             raise ValueError('score must between 0 ~ 100 ')
         else:
             self._score = value


st = Student()
st.score = 70
print st.score