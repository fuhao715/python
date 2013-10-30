# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-10-28
# * Time: 下午3:10
# * To change this template use File | Settings | File Templates.
import types


def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.

    Takes module, class, list, dictionary, or string."""

    # 过滤列表语法：例如可以列表中挑选数据，可列表去重等操作。
    #[mapping-expression for element in source-list if filter-expression]
    method_list = [method for method in dir(object) if callable(getattr(object, method))]
    # 若collapse为真则返回第一个lambda函数,否则返回第二个。其中第一个函数是把s先按空白分割，在同一用空格链接为一行。
    process_func = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" % (method.ljust(spacing),
                                process_func(str(getattr(object, method).__doc__)))
                     for method in method_list])
    gs = ["%s" % (method.ljust(spacing)) for method in method_list if method == 'pop']
    print " ".join(gs)

    method_pop = getattr(object, "pop")  # 获取对象的pop()
    # 调用pop()并打印
    print 'type of method_pop ： %s \n pop :%s \n object is %s \n' % (type(method_pop), method_pop(), object)


def ty(input_string):
    return isinstance(input_string, types.StringType)


if __name__ == "__main__":
    li = ['a', 'b', 'c', 'b', 'abc', 'bed', 'css']
    info(li)
    # 过滤表达式语法，返回列表中不重复的列表
    lin = [elem for elem in li if li.count(elem) == 1]
    print lin

    # and or语法学习
    #and 返回第一个为假的值，若都为真则返回最后一个真值
    print 'a' and 'b'  # 'a'
    print '' and 'a'  # ''
    print 'a' and ''  # ''
    print 'a' and '' and 'c'  # ''
    print 'a' and 'b' and ''  # ''
    #or 返回第一个为真的值，若都为假则返回最后一个假值
    print 'a' or 'b'  # 'a'
    print '' or 'a'  # 'a'
    print 'a' or ''  # 'a'
    print '' or [] or 'c'  # 'c'
    print '' or [] or {}  # '{}'

    # and or使用技巧
    input_str = raw_input("请输入字符：")
    # 1 and a or b 若第一个为真，则返回a否则b，类似 bool ? a : b 表达式
    # 0 and a or b 若第一个为假，则返回b否则a，类似 bool ? a : b 表达式
    res = ty(input_str) and li[0] or li[1]
    print res

    # a 为假则不是预期结果了，可如下办法解决：把a放入列表[a]不为假
    a = ''
    b = 'second'
    result = (1 and [a] or [b])[0]
    print result
