# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
  * User: fuhao
  * Date: 13-2-28 : 下午4:33
'''

# 函数通过def关键字定义。def关键字后跟一个函数的 标识符 名称，然后跟一对圆括号。
# 圆括号之中可以包括一些变量名，该行以冒号结尾。接下来是一块语句，它们是函数体
def sayHello():
    print 'Hello World!' # block belonging to the function

sayHello() # call the function

# 带参数的函数
def printMax(a, b):
    if a > b:
        print a, 'is maximum'
    else:
        print b, 'is maximum'

printMax(3, 4) # directly give literal values

x = 5
y = 7

printMax(x, y) # give variables as arguments

# 局部变量
def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func(x)
print 'x is still', x

# 全局变量

def func():
    global x #表示全局变量，而不是内部变量。

    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func()
print 'Value of x is', x

# 默认参数值
def say(message, times = 1):
    print message * times

say('Hello  中国人')
say('World', 5)

# 如果你的某个函数有许多参数，而你只想指定其中的一部分，
# 那么你可以通过命名来为这些参数赋值——这被称作 关键参数
# 这样做有两个 优势 ——一，由于我们不必担心参数的顺序，使用函数变得更加简单了。
# 二、假设其他参数都有默认值，我们可以只给我们想要的那些参数赋值。
def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c

func(3, 7)
func(25, c=24)
func(c=50, a=100)


