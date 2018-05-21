#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-14 下午5:45
# @Author  : 闫继龙
# @File    : io_text1.py
# @Software: PyCharm

print('-----------------读写文件-----------')

with open('/home/yan/桌面/text.txt', 'r', encoding='UTF-8') as f:
    print(f.read())

'''
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
with open('/Users/michael/test.jpg', 'rb') as f:
    f.read()
'''

# 调用write()来写入文件  ('a' 在文件后面添加字符)
with open('/home/yan/桌面/text.txt', 'w', encoding='UTF-8') as f:
    f.write('Hello world ')

with open('/home/yan/桌面/text.txt', 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        print(line.strip())  ## 把末尾的'\n'删掉

from io import StringIO

print('-----------------读写内存StringIo-----------')
# 写内存数据,StringIO操作的只能是str
f = StringIO()
strByte = f.write('hello')
print(strByte)
print(f.getvalue())  # 方法用于获得写入后的str

# 读内存数据
from io import StringIO

f = StringIO('Hello,\nHi,\nGoodBye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
print()

print('-----------------读写内存BytesIO-----------')

# 操作二进制数据，就需要使用BytesIO
from io import BytesIO

f = BytesIO()
byByte = f.write('中文'.encode('utf-8'))
print(byByte)
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
b = f.read()
print(b)

# 操作文件
print('-----------------  os-----------')
import os

print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('LC_PAPER'))

print('-----------------操作文件和目录-----------')
# 查看当前目录的绝对路径
path = os.path.abspath('.')
print(path)
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
path = os.path.join('/home/yan/temp', 'test')  # 仅仅是表示出路径，并没有创建新目录

# 然后创建一个目录:
isExist = os.path.exists(path)  # 判断文件夹是否存在
if isExist:
    pass  # 存在
else:
    os.mkdir(path)  # 不存在，然后创建一个目录:

# 删掉一个目录:
# os.rmdir('/Users/michael/testdir')

# 使用os.access()方法判断文件是否可进行读写操作。
'''


    os.F_OK: 检查文件是否存在;

    os.R_OK: 检查文件是否可读;

    os.W_OK: 检查文件是否可以写入;

    os.X_OK: 检查文件是否可以执行

'''
if os.access("/home/yan/temp/foo.txt", os.F_OK):
    print("Given file path is exist.")
else:
    print("Given file path not exist.")

if os.access("/home/yan/temp/foo.txt", os.R_OK):
    print("File is accessible to read")
else:
    print("File is not accessible to read")

if os.access("/home/yan/temp/foo.txt", os.W_OK):
    print("File is accessible to write")
else:
    print("File is not accessible to write")

if os.access("/home/yan/temp/foo.txt", os.X_OK):
    print("File is accessible to execute")
else:
    print("File is not accessible to execute")


'''
1. 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
2. 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
3. os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')


'''