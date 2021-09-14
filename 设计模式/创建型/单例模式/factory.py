#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/11 10:06 上午
# @Author : zhenyu lei
# @File : factory.py
# @desc :  工厂模式 - 有一个创建对象的方法
import abc


# abc.ABCMeta 元类，@abc.abstractmethod子类必须实现的方法
class Animal(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def walk(self):
        pass


class Dog(Animal):

    def eat(self):
        print('dog eat')

    def walk(self):
        print('dog walk')


class Cat(Animal):

    def eat(self):
        print('cat eat')

    def walk(self):
        print('cat walk')


class factory(object):

    def __init__(self):
        self.animal_type = None
        self.create_animal_type()

    def create_animal_type(self, object_type):
        if object_type == 'dog':
            self.animal_type = Dog()
        elif object_type == 'cat':
            self.animal_type = Cat()
