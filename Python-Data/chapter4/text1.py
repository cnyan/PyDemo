# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-24 下午8:55
# @Author  : 闫继龙
# @File    : text1.py
# @Software: PyCharm

import numpy as np

# 创建 ndarray
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(['abcd', 123], ndmin=2)
print(arr1)

arr_zero = np.zeros(10)
print(arr_zero)

# 返回垃圾值填充
arr_emp = np.empty((2, 3, 4))
print(arr_emp)

# 对角矩阵
arr_eye = np.eye(4)
print(arr_eye)

# 布尔型索引
names = np.array(['bob', 'joe', 'will', 'bob', 'joe', 'joe', 'alex'])
data = np.random.randn(7, 4)
print(data)

arr_bob = names == 'bob'
print(arr_bob)
print(data[names == 'bob'])

# 矢量化数组运算
points = np.arange(-5, 5, 0.01)  # 1000个间隔相等的点
# print(points)
xs, ys = np.meshgrid(points, points)
print('****' * 10)
print(xs)
print('****' * 10)
print(ys)
# 对该函数进行求值运算
import matplotlib.pyplot as plt

print('****' * 10)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
'''
plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()
plt.show()
'''

print('****' * 10)
# 通用函数
arr = np.random.randn(7) * 5
print(arr)
print(np.modf(arr))

print('****' * 10)
print('python 中的三元表达式 (x if c else y) ')
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result)

print('****' * 10)
print('使用np.where 重现三元表达式')
result = np.where(cond, xarr, yarr)
print(result)

print('****' * 10)
print('使用np.where 通常根据另一个数组而产生新的数组')
arr = np.random.randn(4, 4)
print(arr)
print('使用np.where 将矩阵中的正数替换为2，负值替换为-2')
result = np.where(arr > 0, 2, -2)
print(result)

print('****' * 10)
print('axis = 0 表示y轴求函数')
yresult = result.sum(axis=0)
print(yresult)

print('axis = 1 表示x轴求函数')
xresult = result.sum(axis=1)
print(xresult)

print('****' * 10)
print('使用np 线性代数')
x = np.array([[1, 2., 3], [4, 5, 6.]])
y = np.array([[6., 23], [-1, 7], [8, 9]])
dotResult = x.dot(y)
print(dotResult)

from numpy.linalg import inv, qr, det

print('****' * 10)
print('np.linalg 有一组标准的矩阵分解运算，如求逆和行列式')

x = np.random.randn(5, 5)
print(x)
print()
mat = x.T.dot(x)
print(inv(mat))
print()
print(mat.dot(inv(mat)))
print()
q, r = qr(mat)
print(r)
print()
print(q)
print()
print(det(mat))

print('****' * 10)
print('随机数生成')
from random import normalvariate
import timeit

N = 1000000
sample = [normalvariate(0, 1) for _ in range(N)]

