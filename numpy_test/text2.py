#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-18 下午3:48
# @Author  : 闫继龙
# @File    : text2.py
# @Software: PyCharm

'''
NumPy - 广播

术语广播是指 NumPy 在算术运算期间处理不同形状的数组的能力。
对数组的算术运算通常在相应的元素上进行。
如果两个阵列具有完全相同的形状，则这些操作被无缝执行。
较小的数组会广播到较大数组的大小，以便使它们的形状可兼容。
'''
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a * b)
print(a.ndim)

a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])
print('第一个数组')
print(a)
print('第二个数组')
print(b)
print('a + b')
print(a + b)

#'迭代器对象numpy.nditer。 它是一个有效的多维迭代器对象，可以用于在数组上进行迭代'
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是:')
print(a)

print()
for x in np.nditer(a):
    print(x, end=' ')

print('数组转置')
print(a.T)

print ('以 C 风格顺序排序：')
c = a.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=' ')

print()
print ('以 F 风格顺序排序：')
c = a.copy(order='F')
print(c)
# 显示提醒
for x in np.nditer(a,order='F'):
    print(x, end=' ')
print()

print('==========修改数组的值=========')
for x in np.nditer(a,op_flags=['readwrite']):
    x[...] = x *2
print('修改后的数组是:')
print(a)