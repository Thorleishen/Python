#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/10 10:05 上午
# @Author : zhenyu lei
# @File : singeton.py
# @desc : 单例模式


# 利用类变量可变
class Singeton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class LazySingeton(object):
    """单例模式赖式加载"""
    _instance = None

    def __init__(self):
        if not self._instance:
            print('not init object')
        else:
            print('already init')

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


class SingletonMeta(type):
    """通过元类创建实例 __call__ 魔法方法"""
    __instance = None

    def __init__(self, *args, **kwargs):
        print("__init__")
        super(SingletonMeta, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("__call__")
        if self.__instance is None:
            self.__instance = super(SingletonMeta,self).__call__(*args, **kwargs)
        return self.__instance


class Foo(metaclass=SingletonMeta):
    pass


# 应用场景 (数据库连接池)
"""
只需要创建一个对象，节省内存
数据库连接池（MYSQL、REDIS等）、线程池、缓存、对话框、注册表（服务器健康检查）
"""
class DatabasePool(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    foo1 = Foo()
    foo2 = Foo()
    print(Foo.__dict__)  # 存在一个私有属性来保存属性，而不会污染Foo类（其实还是会污染，只是无法直接通过__instance属性访问）

    print(foo1 is foo2)  # True
