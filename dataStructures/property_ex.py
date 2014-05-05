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

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__





st = Student('michael')
st.score = 70
print st.score
print Student('Amy')
print st



# __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1   # 初始化两个计数器a，b

    def __iter__(self):
        return self     # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b    # 计算下一个值
        if self.a > 100000:     # 退出循环的条件
            raise StopIteration();
        return self.a   # 返回下一个值


for n in Fib():
    print n