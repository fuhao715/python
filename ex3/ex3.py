# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
  * User: fuhao
  * Date: 13-2-28 Time: 下午3:16
'''


# + 加 两个对象相加 3 + 5得到8。'a' + 'b'得到'ab'。
print 3 + 5
print 'a' + 'b'
# - 减 得到负数或是一个数减去另一个数 -5.2得到一个负数。50 - 24得到26。
print 13 - 5
# * 乘 两个数相乘或是返回一个被重复若干次的字符串 2 * 3得到6。'la' * 3得到'lalala'。
print 5 * 6

# ** 幂 返回x的y次幂 3 ** 4得到81（即3 * 3 * 3 * 3）
print 5**6
# / 除 x除以y 4/3得到1（整数的除法得到整数结果）。4.0/3或4/3.0得到1.3333333333333333
print 4/3
print 4.9/3

# // 取整除 返回商的整数部分 4 // 3.0得到1.0
print 5//3
print 7//3.0

# % 取模 返回除法的余数 8%3得到2。-25.5%2.25得到1.5
print 7 % 2
print 23.5 % 1.5

# << 左移 把一个数的比特向左移一定数目（每个数在内存中都表示为比特或二进制数字，即0和1） 2 << 2得到8。——2按比特表示为10
print 2 << 5

# >> 右移 把一个数的比特向右移一定数目 11 >> 1得到5。——11按比特表示为1011，向右移动1比特后得到101，即十进制的5。
print 4 >>4
# & 按位与 数的按位与 5 & 3得到1。
print 4 & 4
# | 按位或 数的按位或 5 | 3得到7。
print 4 | 4
# ^ 按位异或 数的按位异或 5 ^ 3得到6
print 5^3
# ~ 按位翻转 x的按位翻转是-(x+1) ~5得到6。
print ~-7
# < 小于 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。 5 < 3返回0（即False）而3 < 5返回1（即True）。比较可以被任意连接：3 < 5 < 7返回True。
# > 大于 返回x是否大于y 5 > 3返回True。如果两个操作数都是数字，它们首先被转换为一个共同的类型。否则，它总是返回False。
# <= 小于等于 返回x是否小于等于y x = 3; y = 6; x <= y返回True。
# >= 大于等于 返回x是否大于等于y x = 4; y = 3; x >= y返回True。
# == 等于 比较对象是否相等 x = 2; y = 2; x == y返回True。x = 'str'; y = 'stR'; x == y返回False。x = 'str'; y = 'str'; x == y返回True。
# != 不等于 比较两个对象是否不相等 x = 2; y = 3; x != y返回True。
# not 布尔“非” 如果x为True，返回False。如果x为False，它返回True。 x = True; not y返回False。
x = True
print not x

# and 布尔“与” 如果x为False，x and y返回False，否则它返回y的计算值。 x = False; y = True; x and y，由于x是False，返回False。在这里，Python不会计算y，因为它知道这个表达式的值肯定是False（因为x是False）。这个现象称为短路计算。
y = False
print x and y

# or 布尔“或” 如果x是True，它返回True，否则它返回y的计算值。 x = True; y = False; x or y返回True。短路计算在这里也适用。
print x or y


