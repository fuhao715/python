# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 14-3-7
# * Time: 上午10:54
# * To change this template use File | Settings | File Templates.
import time


def now1():
    print time.strftime('%Y-%m-%d', time.localtime(time.time()))


# 装饰器decorator，在不改变now函数情况下，在打印前后log信息,需要定义在now()前面
def my_log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@my_log
def now():
    print time.strftime('%Y-%m-%d', time.localtime(time.time()))

now()


# 如果decorator本身需要传入参数，那就需要返回decorator的高阶函数，比如，要自定义log的文本：
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log2('execute')
def now2():
    print time.strftime('%Y-%m-%d', time.localtime(time.time()))

now2()

n = log2('executes')(now1)
n()
print n.__name__