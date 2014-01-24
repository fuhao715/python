# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
  * User: fuhao
  * Date: 13-3-11 : 下午8:34
'''
#!/usr/bin/python
# Filename: func_doc.py
import logging
import os

def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

printMax(3, 5)
print printMax.__doc__

logging.basicConfig(filename=os.path.join(os.getcwd(), 'log.txt'), level=logging.WARN, format='%(asctime)s - %(levelname)s: %(message)s')
logging.debug('this is a debug message')
logging.debug('debug')  #被忽略
logging.info('info')    #被忽略
logging.warning('warn')
logging.error('error')
