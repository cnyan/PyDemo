# -*- coding:utf-8 -*-
# !/usr/bin/python3


# ctrl + alt + l 格式化代码

def product(x, *y):
    for n in y:
        x = x * n
    return x


print(product(5, 6))

# 字符格式化
strFormat = 'Hello, {0},成绩提升{1:.1f}%'.format("小明", 17.242)
print(strFormat)


# 递归函数 计算 n！  fact(n) = n! = 1*2*3*……*(n-1)*n = (n-1)!*n = fact(n-1)*n
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print('50!是:%d' % fact(50))


# 定义函数，去除字符串收尾的空格
def trim(s):
    while (s[0:1] == ' '):
        s = s[1:]
    while (s[-1:-2] == ' '):
        s = s[:-2]
    return s


print(trim(' ABCD'))


# 利用迭代查找list中最小值和最大值
def findMinAndMax(L):
    if (len(L)):
        min, max = L[0], L[0]
        for v in L:
            if min > v:
                min = v
            if max < v:
                max = v
        return min, max
    else:
        return None, None


print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([3, 9, 5, 10, 2, 5, 5]))

# 列表生成式
l = [x * x for x in range(1, 11)]
print(l)
l = [x * x for x in range(1, 11) if x % 2 == 0]
print(l)
# 双层嵌套，生成全排列
l = [m + n for m in 'ABC' for n in 'XYZ']
print(l)

# 列出当前目录下的所有文件和目录名
import os

l = [d for d in os.listdir('.')]
print(l)