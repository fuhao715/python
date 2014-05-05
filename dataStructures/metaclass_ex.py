# -*- coding: utf-8 -*-
__author__ = 'fuhao'
'''
 * Created with PyCharm.
 * User: fuhao
 * Date: 14-5-5
 * Time: 下午8:17
 * To change this template use File | Settings | File Templates.
'''
# metaclass是创建类，所以必须从`type`类型派生：
'''
当我们写下__metaclass__ = ListMetaclass语句时，魔术就生效了，
它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：
1、当前准备创建的类的对象；
2、类的名字；
3、类继承的父类集合；
4、类的方法集合。
'''
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value : self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类

L = MyList()
L.add(1)
print L