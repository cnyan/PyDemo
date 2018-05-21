#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-14 下午3:30
# @Author  : 闫继龙
# @File    : text2.py
# @Software: PyCharm


'a test module'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')



print(range(9))
print(type(range(9)))

import numpy as np

print(np.arange(10))
print(type(np.arange(10)))
