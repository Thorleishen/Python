#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/10 5:05 下午
# @Author : zhenyu lei
# @File : metaobject.py
# @desc : 元类
import abc


class Mymeta(type):

    def __new__(cls, *args, **kwargs):
        obj = super(Mymeta, cls).__new__(cls, *args, **kwargs)
        print('===>Mymeta.__new__')
        return obj

    def __init__(self, name, bases, dic):
        super().__init__(name, bases, dic)
        print('===>Mymeta.__init__')
        print(self.__name__)
        print(dic)
        print(self.yaml_tag)

    def __call__(self, *args, **kwargs):
        print('===>Mymeta.__call__')
        obj = super(Mymeta, self).__call__(*args, **kwargs)
        return obj


class Foo(metaclass=Mymeta):
    yaml_tag = '!Foo'

    def __init__(self, name):
        print('Foo.__init__')

        self.name = name

    def __new__(cls, *args, **kwargs):
        print('Foo.__new__')

        return object.__new__(cls)


if __name__ == '__main__':
    foo = Foo('foo')
