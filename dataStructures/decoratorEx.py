# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 14-3-7
# * Time: 上午10:54
# * To change this template use File | Settings | File Templates.
import time

# 装饰器decorator，在不改变now函数情况下，在打印前后log信息,需要定义在now()前面
def my_log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@my_log
def now():
    print time.strftime('%Y-%m-%d',time.localtime(time.time()))

now()