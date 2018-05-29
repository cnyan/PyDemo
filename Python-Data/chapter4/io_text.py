#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-28 上午10:59
# @Author  : 闫继龙
# @File    : io_text.py
# @Software: PyCharm

'''
使用 numpy 实现文件的输入输出
np.save 和 np.load 是读写磁盘数组数据的两个主要函数
默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为 .npy的文件中的
'''

import numpy as np

arr = np.arange(10)
np.save('../src/io_numpy_npy', arr)
# 读取文件
text = np.load('../src/io_numpy_npy.npy')
print(text)

print('=================将多个数组保存到一个压缩文件中================')
np.savez('../src/io_numpy_npz', a=arr, b=arr)
# 读取文件，加载.npz　文件时，会得到一个类似字典的对象
arch = np.load('../src/io_numpy_npz.npz')
for text in arch:  # 读取字典
    print(text)  # 获取key值
    print(arch[text])  # 读取文件

'''
利用 pandas　读取本地文件
read_csv,和read_table函数　读取文件
np.loadtxt,和np.genfromtxt 将数据加载到普通的numpy数组中
'''

