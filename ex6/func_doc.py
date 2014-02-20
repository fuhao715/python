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
import logging.handlers
import glob

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

log_file = os.path.join(os.getcwd(), 'log.txt')
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

my_log = logging.getLogger("MyLogger")
my_log.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
my_log.addHandler(handler)

#ch = logging.StreamHandler()
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#ch.setFormatter(formatter)
#my_log.addHandler(ch)

my_log.debug('this is a debug message')
my_log.debug('debug')  #被忽略
my_log.info('info')    #被忽略
my_log.warning('warn')
my_log.error('error')
pid = 12
message = "message "
my_log.debug('debug soffice pid = %d msg=%s ', pid, message)

logfiles = glob.glob('%s*' % log_file)

for filename in logfiles:
    print(filename)
