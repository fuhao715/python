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

l = [x*x for x in range(10)]
print l
g = (x*x for x in range(10))
print g, g.next()

print '----------'
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