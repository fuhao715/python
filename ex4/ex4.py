# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
  * User: fuhao
  * Date: 13-2-28 : 下午3:33
'''
# if语句用来检验一个条件， 如果 条件为真，我们运行一块语句（称为 if-块 ）， 否则 我们处理另外一块语句（称为 else-块 ）。 else 从句是可选的。

number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number :
    print 'ok'
elif guess < number:
    print '<'
else:
    print '>'

print 'done '

# while语句 只要在一个条件为真的情况下，while语句允许你重复执行一块语句。while语句是所谓 循环 语句的一个例子。while语句有一个可选的else从句
running = True

while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.'
        running = False # this causes the while loop to stop
    elif guess < number:
        print 'No, it is a little higher than that'
    else:
        print 'No, it is a little lower than that'
else:
    print 'The while loop is over.'
    # Do anything else you want to do here

print 'Done'

# for循环：for..in是另外一个循环语句，它在一序列的对象上 递归 即逐一使用队列中的每个项目
for i in range(0,9):
    print i
else:
    print 'Done'