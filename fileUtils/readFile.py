# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-10-11
# * Time: 下午3:03
# * To change this template use File | Settings | File Templates.
from sys import argv
script, filename = argv

txt = open(filename)

print "read 读取文件名为：%r:" % filename
print txt.read()

print "再读取一遍文件: "
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()

print 'done'