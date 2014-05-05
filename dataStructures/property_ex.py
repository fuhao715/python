# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 14-5-5
 * Time: 下午3:32
 * To change this template use File | Settings | File Templates.
'''
import types


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

    def __call__(self):
        print('My name is %s.' % self.name)





st = Student('michael')
st.score = 70
print st.score
print Student('Amy')
print st
print st(), 'st()', callable(Student('Jack'))



# __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1   # 初始化两个计数器a，b

    def __iter__(self):
        return self     # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b    # 计算下一个值
        if self.a > 100000:     # 退出循环的条件
            raise StopIteration()
        return self.a   # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop + 1):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print n


f = Fib()
print f[1], f[100],f[0:5],f[:10:2]



class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def user(self, name):
        import sys
        fn_name = (lambda:sys._getframe(1).f_code.co_name)()
        return Chain('%s/%s/:%s' % (self._path, fn_name, name))

print Chain().status.user('fuhao').timeline.list
# /status/user/:fuhao/timeline/list