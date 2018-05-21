#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-14 下午4:36
# @Author  : 闫继龙
# @File    : Chain.py
# @Software: PyCharm

'''
利用完全动态的__getattr__，我们可以写出一个链式调用：
给每个URL对应的API都写一个方法
'''


class Chain(object):

    def __init__(self, path='GET'):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    # 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
    def __call__(self, args):
        return Chain('%s/%s' % (self._path, args))

    def __str__(self):
        return self._path

    __repr__ = __str__


c = Chain().status.user.timeline.list
print(c)
print(Chain().users('michael').repos)

'''
__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
'''
chain = Chain('repos')
print(chain('test'))  # 直接把实例对象当做函数调用，对象看成函数
# 把函数看成对象，因为这两者之间本来就没啥根本的区别

from enum import Enum

Month = Enum('Month', ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'))
for name, member in Month.__members__.items():
    print(name, '=>', ',', member.value)

print(Month.mar)
