#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-15 上午9:52
# @Author  : 闫继龙
# @File    : Query.py
# @Software: PyCharm

'''
并不是只有open()函数返回的fp对象才能使用with语句。
实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。

实现上下文管理是通过__enter__和__exit__这两个方法实现的。
例如，下面的class实现了这两个方法：

'''


class Query(object):
    def __init__(self, name):
        self.__name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.__name)


with Query('Bob') as q:
    q.query()