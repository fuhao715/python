# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 14-3-14
# * Time: 下午4:02
# * To change this template use File | Settings | File Templates.
import time

'''
上下文管理器被with声明所激活，这个API涉及到两个方法。
1. __enter__方法，当执行流进入with代码块时，__enter__方法将执行。并且它将返回一个可供上下文使用的对象。
2. 当执行流离开with代码块时，__exit__方法被调用，它将清理被使用的资源。
'''
class demo():
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print('{}: {}').format(self.label, end - self.start)

with demo('counting'):
    n = 10000000
    while n > 1:
        n -= 1

# 利用@contextmanager装饰器
from contextlib import contextmanager

@contextmanager
def demo_context(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}').format(label, end - start)


with demo_context('counting'):
    n = 10000000
    while n > 1:
        n -= 1

