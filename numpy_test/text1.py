#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-17 下午3:56
# @Author  : 闫继龙
# @File    : text1.py
# @Software: PyCharm


import numpy as np

a = np.array([[1, 2, 4, 8], [3, 4, 5, 6]])
print(a)

print(a.shape)
print(type(a))
print(a.dtype)

# 最小维度(行）
a = np.array([1, 2, 3, 4, 5], ndmin=3, dtype=complex)
print(a)

a = np.arange(24)
print(a.ndim)
# 现在调整其大小
b = a.reshape(2, 4, 3)
print(b)
# b 现在拥有三个维度
print(b.ndim)

b = a.reshape(4, 3, 2)
print(b)
# b 现在拥有三个维度
print(b.ndim)
# 这一数组属性返回数组中每个元素的字节单位长度。
print(b.itemsize)

print(b.flags)

# numpy.empty .它创建指定形状和dtype的未初始化数组。 它使用以下构造函数：
x = np.empty([3, 2], float, 'C')
print(x)

# numpy.zeros返回特定大小，以 0 填充的新数组
x = np.zeros([3, 3, 2], int)
print(x)
# 自定义类型
x = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(x)

print()
y = np.asarray(x, dtype=float)
print(y)

print()
# numpy.frombuffer 此函数将缓冲区解释为一维数组。
# 暴露缓冲区接口的任何对象都用作参数来返回ndarray。
s = b'Hello World'
try:
    a = np.frombuffer(s, dtype='S1')  # 'S', 'a'：字节串
    print(a)
except AttributeError as ae:
    print(ae)
finally:
    print('end')

# numpy.fromiter,此函数从任何可迭代对象构建一个ndarray对象，
# 返回一个新的一维数组。
it = iter(s)
a = np.fromiter(it, dtype='S1')
print(a)

print('===========NumPy - 切片和索引===========')
a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])
print(a[2:7:2])

print('二维数组切片')
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[1:2])

print('切片还可以包括省略号(...)，来使选择元组的长度与数组的维度相同。 '
      '如果在行位置使用省略号，它将返回包含行中元素的ndarray。')

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('源数组是:')
print(a)

# 这会返回第二列元素的数组
print('第二列的元素是:')
print(a[..., 1])
print()

# 现在我们从第二行切片所有元素：
print('第二行的元素是:')
print(a[1, ...])

print('第二列及剩余的元素是:')
print(a[..., 1:])

print('第二行及剩余的元素是:')
print(a[1:])

print('===整数索引========')
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]  # 该结果包括数组中(0,0)，(1,1)和(2,0)位置处的元素。
print(y)  # [1 4 5]

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
rows = np.array([[0, 0], [3, 3]])
lows = np.array([[0, 2], [0, 2]])
print('行数列：')
print(rows)
print('列数列')
print(lows)
y = x[rows, lows]
print('这个数组的每个角处的元素是:')
print(y)

'''
使用slice作为列索引和高级索引。
当切片用于两者时，结果是相同的。 
但高级索引会导致复制，并且可能有不同的内存布局。
'''

print()
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
# 切片
z = x[1:4, 1:3]
print('切片之后，我们的数组变为：')
print(z)

print('对列使用高级索引来切片：')
y = x[1:4, [1, 2]]
print(y)

print()
print('==当结果对象是布尔运算(例如比较运算符)的结果时，将使用此类型的高级索引。===')
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)

print('大于 5 的元素是：')
print(x[x > 5])
