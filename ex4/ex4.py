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
'''
我们所做的只是提供两个数，range返回一个序列的数。这个序列从第一个数开始到第二个数为止。
例如，range(1,5)给出序列[1, 2, 3, 4]。默认地，range的步长为1。如果我们为range提供第三个数，那么它将成为步长。
例如，range(1,5,2)给出[1,3]。记住，range 向上 延伸到第二个数，即它不包含第二个数。
for循环在这个范围内递归——for i in range(1,5)等价于for i in [1, 2, 3, 4]，
这就如同把序列中的每个数（或对象）赋值给i，一次一个，然后以每个i的值执行这个程序块。
在这个例子中，我们只是打印i的值。
记住，else部分是可选的。如果包含else，它总是在for循环结束后执行一次，除非遇到break语句。

'''
for i in range(0,9):
    print i
else:
    print 'Done'


# break 、continue
while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    print 'Length of the string is', len(s)
print 'Done'


while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print 'Input is of sufficient length'
    # Do other kinds of processing here...