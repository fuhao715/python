# -*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'fuhao'
'''
  PROJECT_NAME:python
  PACKAGE_NAME:
  File_Name:reference.py
  User: fuhao
  Date: 13-3-15 : 下午3:57
  descripton:
'''
from collections import Iterable
print 'Simple Assignment'
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist  # mylist is just another name pointing to the same object!

if isinstance(shoplist, Iterable):
    print 'yes'
    for value in shoplist:
        print value, "---"

#列表推导表达式
l = [x*x for x in range(10) if x > 5]
print l
#生成器表达式同列表推导式有着几乎相同的语法结构，区别在于生成器表达式是被圆括号包围，而不是方括号：
g = (x*x for x in range(10) if x > 5)
print g, g.next()

print '----------'

# yield 简单说来就是一个生成器，生成器是这样一个函数，它记住上一次返回时在函数体中的位置。
# 对生成器函数的第二次（或第 n 次）调用跳转至该函数中间，而上次调用的所有局部变量都保持不变。
def fab(res):
    n, a, b = 0, 0, 1
    while n < res:
        yield b
        a, b = b, a + b
        n = n+1

fa = fab(6)
print fa
for v in fa:
    print v

print '----------'
del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object

print 'Copy by making a full slice'
mylist = shoplist[:] # make a copy by doing a full slice
del mylist[0] # remove first item

print 'shoplist is', shoplist
print 'mylist is', mylist
# notice that now the two lists are different