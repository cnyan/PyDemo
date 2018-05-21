#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-15 上午9:21
# @Author  : 闫继龙
# @File    : module_text.py
# @Software: PyCharm

from datetime import datetime

'''
str转换为datetime 转换方法是通过datetime.strptime()实现
datetime转换为str 转换方法是通过strftime()实现的
'''
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now)

'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，
并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
'''
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

# 以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
import hashlib
md5pwd = hashlib.md5()
md5pwd.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5pwd.hexdigest())