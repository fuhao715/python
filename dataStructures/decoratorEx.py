# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 14-3-7
# * Time: 上午10:54
# * To change this template use File | Settings | File Templates.
import time
import functools


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


# 如果decorator本身需要传入参数，那就需要返回decorator的高阶函数，比如，要自定义log的文本
# 查询一下my_log.__name__的话，你会发现其输出的是“wrapper”，而不是我们期望的：
# Python的functool包中提供了一个叫wrap的decorator来消除这样的副作用。
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'before %s %s %s():' % (time.strftime('%Y-%m-%d', time.localtime(time.time())), text, func.__name__)
            res = func(*args, **kw)
            print 'after %s  %s %s():' % (time.strftime('%Y-%m-%d', time.localtime(time.time())), text, func.__name__)
            return res
        return wrapper
    return decorator


@log2('execute')
def now2():
    print 'this ', time.strftime('%Y-%m-%d', time.localtime(time.time()))

now2()

n = log2('executes')(now1)
n()
print n.__name__

# 当然，即使是你用了functools的wraps，也不能完全消除这样的副作用。
# from inspect import getmembers, getargspec
import inspect

def wraps_decorator(f):
    @functools.wraps(f)
    def wraps_wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wraps_wrapper

class SomeClass(object):
    @wraps_decorator
    def method(self, x, y):
        pass

obj = SomeClass()
for name, func in inspect.getmembers(obj, predicate=inspect.ismethod):
    print "Member Name: %s" % name
    print "Func Name: %s" % func.func_name
    print "Args: %s" % inspect.getargspec(func)[0]

# 输出：
# Member Name: method
# Func Name: method
# Args: []
# 要修正这一问，我们还得用Python的反射来解决，下面是相关的代码：
def get_true_argspec(method):
    argspec = inspect.getargspec(method)
    args = argspec[0]
    if args and args[0] == 'self':
        return argspec
    if hasattr(method, '__func__'):
        method = method.__func__
    if not hasattr(method, 'func_closure') or method.func_closure is None:
        raise Exception("No closure for method.")

    method = method.func_closure[0].cell_contents
    return get_true_argspec(method)


def dec(func):
    def modify(*args, **kwargs):
        variable = kwargs.pop('variable', None)
        print variable
        x, y = func(*args, **kwargs)
        return x, y
    return modify

@dec
def func_sqrt(x, y):
    print x**2, y**3
    return x**2, y**3

func_sqrt(x=2, y=3, variable='variable')
func_sqrt(x=4, y=5)

def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
                                     if "css_class" in kwds else ""
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">" + fn(*args, **kwds) + "</"+tag+">"
        return wrapped
    return real_decorator

@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"

print hello()

# 输出：
# <b class='bold_css'><i class='italic_css'>hello world</i></b>


class myDecorator(object):

    def __init__(self, fn):
        print "inside myDecorator.__init__()"
        self.fn = fn

    def __call__(self):
        self.fn()
        print "inside myDecorator.__call__()"

@myDecorator
def aFunction():
    print "inside aFunction()"

print "Finished decorating aFunction()"

aFunction()

# 输出：
# inside myDecorator.__init__()
# Finished decorating aFunction()
# inside aFunction()
# inside myDecorator.__call__()


'''
上面这段代码中，我们需要注意这几点：
1）如果decorator有参数的话，__init__() 成员就不能传入fn了，而fn是在__call__的时候传入的。
2）这段代码还展示了 wrapped(*args, **kwargs) 这种方式来传递被decorator函数的参数。
（其中：args是一个参数列表，kwargs是参数dict）
'''
class makeHtmlTagClass(object):

    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
                                       if css_class !="" else ""

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class+">"  \
                       + fn(*args, **kwargs) + "</" + self._tag + ">"
        return wrapped

@makeHtmlTagClass(tag="b", css_class="bold_css")
@makeHtmlTagClass(tag="i", css_class="italic_css")
def hello(name):
    return "Hello, {}".format(name)

print hello("Hao Chen")

# 用Decorator设置函数的调用参数
# 第一种，通过 **kwargs，这种方法decorator会在kwargs中注入参数。
def decorate_A(function):
    def wrap_function(*args, **kwargs):
        kwargs['str'] = 'Hello!'
        return function(*args, **kwargs)
    return wrap_function

@decorate_A
def print_message_A(*args, **kwargs):
    print(kwargs['str'])

print_message_A()

# 第二种，约定好参数，直接修改参数
def decorate_B(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        return function(str, *args, **kwargs)
    return wrap_function

@decorate_B
def print_message_B(str, *args, **kwargs):
    print(str)

print_message_B()


# 第三种，通过 *args 注入
def decorate_C(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        #args.insert(1, str)
        args = args +(str,)
        return function(*args, **kwargs)
    return wrap_function

class Printer:
    @decorate_C
    def print_message(self, str, *args, **kwargs):
        print(str)

p = Printer()
p.print_message()

# 一些decorator的示例
# 给函数调用做缓存
from functools import wraps
def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper

@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
# 讲解
'''
上面这个例子中，是一个斐波拉契数例的递归算法。我们知道，这个递归是相当没有效率的，因为会重复调用。
比如：我们要计算fib(5)，于是其分解成fib(4) + fib(3)，而fib(4)分解成fib(3)+fib(2)，
fib(3)又分解成fib(2)+fib(1)…… 你可看到，基本上来说，fib(3), fib(2), fib(1)在整个递归过程中被调用了两次。

而我们用decorator，在调用函数前查询一下缓存，如果没有才调用了，有了就从缓存中返回值。
一下子，这个递归从二叉树式的递归成了线性的递归。
'''

# Profiler的例子
import cProfile, pstats, StringIO

def profiler(func):
    def wrapper(*args, **kwargs):
        datafn = func.__name__ + ".profile" # Name the data file
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        #prof.dump_stats(datafn)
        s = StringIO.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(prof, stream=s).sort_stats(sortby)
        ps.print_stats()
        print s.getvalue()
        return retval

    return wrapper



