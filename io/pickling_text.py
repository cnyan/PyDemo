#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-14 下午8:38
# @Author  : 闫继龙
# @File    : pickling_text.py
# @Software: PyCharm

'''
我们把变量从内存中变成可存储或传输的过程称之为序列化，
在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等，
都是一个意思。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
'''

import os

path = os.path.join('/home/yan/temp', 'dump.txt')
if os.path.exists(path):
    pass
else:
    os.mkdir(path)

import pickle

d = dict(name='Bob', age=20, score=90)
byteResult = pickle.dumps(d)
print(byteResult)

# pickle.dumps()方法把任意对象序列化成一个bytes
# dump() 然后就可以把二进制写进文件
with open('/home/yan/temp/dump.txt', mode='wb') as f:
    pickle.dump(d, f)

# 反序列操作,直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
print()
with open('/home/yan/temp/dump.txt', mode='rb') as f:
    d = pickle.load(f)

print(d)















