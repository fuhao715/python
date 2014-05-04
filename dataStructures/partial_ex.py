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

int2 = functools.partial(int, base = 2)

print int2('100000')