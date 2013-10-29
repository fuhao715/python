# -*- coding: UTF-8 -*-
__author__ = 'fuhao'
# * Created by PyCharm.
# * User: fuhao
# * Date: 13-10-28
# * Time: 下午3:10
# * To change this template use File | Settings | File Templates.


def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.

    Takes module, class, list, dictionary, or string."""

    # 过滤列表语法：例如可以列表中挑选数据，可列表去重等操作。
    #[mapping-expression for element in source-list if filter-expression]
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" % (method.ljust(spacing),
                                processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])
    gs = ["%s" % (method.ljust(spacing)) for method in methodList if method == 'pop']
    print " ".join(gs)

    method_pop = getattr(object, "pop")  # 获取对象的pop()
    # 调用pop()并打印
    print 'type of method_pop ： %s \n pop :%s \n object is %s \n' % (type(method_pop),method_pop(), object)

if __name__ == "__main__":
    li = ['a', 'b', 'c', 'b', 'abc', 'bed', 'css']
    info(li)
    # 过滤表达式语法，返回列表中不重复的列表
    lin = [elem for elem in li if li.count(elem) == 1]
    print lin

