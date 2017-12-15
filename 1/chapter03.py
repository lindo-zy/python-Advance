#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 面向对象

# 动态绑定    __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Alice'
s.age = 25
print(s.name, s.age)


# @property装饰器就是负责把一个方法变成属性调用的
class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def resolution(self):
        return self.width * self.height

    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)

# 定制类

# __iter__
'''
如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法
'''


# 斐波那契数列
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)

# 使用枚举类
from enum import Enum


class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
for name, i in Color.__members__.items():
    print(name, i.value)
'''
定义枚举时，成员名称不允许重复
如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员
如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique【要导入unique模块】
'''