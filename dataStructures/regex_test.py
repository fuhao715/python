# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 2014/6/2
 * Time: 21:52
 * To change this template use File | Settings | File Templates.
'''
import re

if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print 'ok'

if re.match(r'^\d{3}\-\d{3,8}$', '010 12345'):
    print 'ok'
else:
    print 'failed'

print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,\;]+', 'a,b;; c  d')

ma = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print ma.groups()
print ma.group(0)
print ma.group(1)
print ma.group(2)

# 贪婪匹配，默认
print re.match(r'^(\d+)(0*)$', '102300').groups()

# 非贪婪匹配，需要加?即可
print re.match(r'^(\d+?)(0*)$', '102300').groups()

# 预编译正则匹配表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()
print re_telephone.match('010-8086').groups()

