# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-10-29
# * Time: 上午11:04
# * To change this template use File | Settings | File Templates.
import game.compute as compute


def output(first, second, formate="plus"):
    # 第三个参数为默认值，若未输入第三个参数则返回默认值。
    output_function = getattr(compute, formate, compute.plus(first, second))
    return output_function(first, second)


if __name__ == "__main__":
    a = int(raw_input("请输入第一个数："))
    b = int(raw_input("请输入第二个数："))
    c = raw_input("请输入plus、subtract、multiply、divide计算类型：")
    print 'c is %r' % c
    if c == '':
        print output(a, b)
    else:
        print output(a,b,c)