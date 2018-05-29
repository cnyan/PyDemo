#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-28 下午3:45
# @Author  : 闫继龙
# @File    : text1.py
# @Software: PyCharm

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

print('======Series===========')
obj = Series([4, 7, -5, 3])
print(obj)

print(obj.index)
print(obj.values)

print('========' * 10)
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)

print('========' * 10)
isTrue = 'b' in obj2
print(isTrue)

print('========' * 10)
# print(obj + obj2)

print('========' * 10)
print(obj2.name)
print(obj2.index.name)

print('========' * 10)
obj2.name = 'name_name'
obj2.index.name = 'name_index'
print(obj2)

print('====DataFrame 是一个表格型的数据结构====')
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)

frame2 = DataFrame(data, columns=['year', 'state', 'pop'],
                   index=['a', 'b', 'c', 'd', 'e'])
frame3 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['a', 'b', 'c', 'd', 'e'])

frame3['debt'] = np.arange(5)

arr = np.arange(9).reshape(3, 3)
frame4 = DataFrame(arr, columns=['a', 'b', 'c'])

index = pd.Index(['f'])
print('========' * 10)
frame5 = frame4.reindex(index=['a', 'b', 'c', 'd', 'e'], fill_value='404',
                        columns=['col1', 'col2', 'col3', 'col4'])
print(frame5)

print('============= Series 索引 ============')
obj = Series(np.arange(4), index=['a', 'b', 'c', 'd'])

obj[['a', 'c', 'b']]  # 参数是一个队列,二维队列

print('===================算术运算和数据对齐=============')
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
# 自动对齐的操作在不重复的索引处，引入了NA值

df1 = DataFrame(np.arange(9).reshape(3, 3), columns=list('bcd'),
                index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12).reshape(4, 3), columns=list('bde'),
                index=['Utah', 'Ohio', 'Texas', 'Oregon'])

series = df1.loc['Ohio']  # = df1.iloc[0]
f = lambda x: x.max() - x.min()
df1.apply(f)
df1.apply(f, axis=1)

print('=============排名和排序 =====')

'''
sort_index(axis=0) 是按照索引排序
sort_value(axis=0) 是按照值排序

sort_index(by='b') 是按照 b列排序
sort_index(by=['a','b']) 是按照 多个[a,b]列排序
'''

print('==== rank 排名====' * 10)
obj = Series([7, -5, 7, 4, 2, 0, 4])
print('排名（Series.rank(method=average, ascending=True)）'
      '的作用与排序的不同之处在于，'
      '他会把对象的 values 替换成名次（从 1 到 n）。'
      '这时唯一的问题在于如何处理平级项，'
      '方法里的 method 参数就是起这个作用的，'
      '他有四个值可选：average, min, max, first。')
print('排名具体默认具体方法是'
      '将源数组降序，按照源数组的数据 比对排名顺序')

print('========== 相关系数和协方差 =========')


import pandas_datareader as pdr

all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = pdr.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')

price = DataFrame({tic: data['Adj close'] for tic, data in all_data})
print('========' * 10)

print('========' * 10)

print('========' * 10)

print('========' * 10)

print('========' * 10)
