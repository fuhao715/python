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
txt.close()
print "再读取一遍文件: "
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
print 'done'


def print_more(*args):
    first, second, third = args
    print '%s,%s,%s' % (first, second, third)
    return first, second, third

first_str, second_str, third_str = print_more('f', 'se', 'th')
print 'print again %s,%s,%s' % (first_str, second_str, third_str)