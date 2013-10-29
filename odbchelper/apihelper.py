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

    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" % (method.ljust(spacing),
                                processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])
    gs = ["%s" % (method.ljust(spacing)) for method in methodList if method == 'pop']
    print " ".join(gs)

    method_pop = getattr(object, "pop")
    print 'type of method_pop ： %s \n pop :%s \n object is %s \n' % (type(method_pop),method_pop(), object)

if __name__ == "__main__":
    li = ['a', 'b', 'c']
    info(li)

