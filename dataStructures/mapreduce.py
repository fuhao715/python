# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 14-3-6
# * Time: 下午3:40
# * To change this template use File | Settings | File Templates.


def sqr(x):
    return x * x

res = map(sqr, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print res


def add(x, y):
    return x + y

result = reduce(add, [1, 3, 5, 7, 9])
print result


# 把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x, y):
    return 10*x + y
print reduce(fn, [1, 3, 5, 7, 9])


# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
print reduce(fn, map(int, '13579'))
# 分解字符串为一个个数字List
print map(int, '13579')


def str2int1(s):
    def fs(x, y):
        return x * 10 + y
    return reduce(fs, map(int, s))
print str2int1('13579')


def str2int(s):
    return reduce(lambda x, y: x*10+y, map(int, s))


print str2int('13579')

# python中除了list、dict是对象类型，在函数中是传递引用地址，其余的全部是传值，复制副本传递给函数。
def test1(x):
    print x, id(x)
    x = x.upper()
    print x, id(x)
    return x

a = 'a'
print a, id(a)
test1(a)
print a, id(a)


# list ['a','b',2,4,'abc','efg']
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复.set([1, 2, 3])
# *args是可变参数，args接收的是一个tuple；(1,2,3)
#**kw是关键字参数，kw接收的是一个dict。{'a': 1, 'b': 2}
# python高阶函数之函数传递、返回
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax +n
    return ax


def lazy_sum(*args):
    def sum_later():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum_later

print calc_sum(1, 3, 5, 7, 9)
print lazy_sum(1, 3, 5, 7, 9)
print lazy_sum(1, 3, 5, 7, 9)()

#匿名函数
complex_num = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print complex_num
f = lambda x: x + 10
print f(2)


def build(x, y):
    return lambda: x * x + y * y

fun = build(3, 6)
print fun, fun()
