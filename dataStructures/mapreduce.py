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


name_len = map(len, ["hao", "chen", "coolshell"])
print name_len
# 输出 [3, 4, 9]

def toUpper(item):
      return item.upper()

upper_name = map(toUpper, ["hao", "chen", "coolshell"])
print upper_name
# 输出 ['HAO', 'CHEN', 'COOLSHELL']

squares = map(lambda x: x * x, range(9))
print squares
# 输出 [0, 1, 4, 9, 16, 25, 36, 49, 64]

print reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# 输出 15


# 计算数组中正数的平均值
num =[2, -5, 9, 7, -2, 5, 3, 1, 0, -3, 8]
positive_num_cnt = 0
positive_num_sum = 0
for i in range(len(num)):
    if num[i] > 0:
        positive_num_cnt += 1
        positive_num_sum += num[i]

if positive_num_cnt > 0:
    average = positive_num_sum / positive_num_cnt

print average
# 输出 5

# 用函数式编程则简易很多,两行代码搞定
positive_num_sum = filter(lambda x: x > 0, num)
average = reduce(lambda x, y: x + y, positive_num_sum)/len(positive_num_sum)
print average

''' 函数式编程有如下好处：
1）代码更简单了。
2）数据集，操作，返回值都放到了一起。
3）你在读代码的时候，没有了循环体，于是就可以少了些临时变量，以及变量倒来倒去逻辑。
4）你的代码变成了在描述你要干什么，而不是怎么去干。
'''

from random import random

def move_cars(car_positions):
    return map(lambda x: x + 1 if random() > 0.3 else x,
               car_positions)

def output_car(car_position):
    return '-' * car_position

def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}

def draw(state):
    print ''
    print '\n'.join(map(output_car, state['car_positions']))

def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))

race({'time': 5,
      'car_positions': [1, 1, 1]})



# 利用yield关键字返回一个Generator
def even_filter(nums):
    for num in nums:
        if num % 2 == 0:
            yield num
def multiply_by_three(nums):
    for num in nums:
        yield num * 3
def convert_to_string(nums):
    for num in nums:
        yield 'The Number: %s' % num

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = convert_to_string(multiply_by_three(even_filter(nums)))
for num in pipeline:
    print num
# 输出：
# The Number: 6
# The Number: 12
# The Number: 18
# The Number: 24
# The Number: 30

# 利用map&Reduce方式实现
def even_filter_1(nums):
    return filter(lambda x: x %2 == 0, nums)

def multiply_by_three_1(nums):
    return map(lambda x: x *3, nums)

def convert_to_string_1(nums):
    return map(lambda x: 'The number : %s ' % x, nums)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = convert_to_string_1(multiply_by_three_1(even_filter_1(nums)))
for num in pipeline:
    print num

print '-------------'
# 他们的代码需要嵌套使用函数，这个有点不爽，如果我们能像下面这个样子就好了
def pipeline_func(data, fns):
    return reduce(lambda a, x: x(a), fns, data)

print pipeline_func(nums, [even_filter_1, multiply_by_three_1, convert_to_string_1])
