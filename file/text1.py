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

# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(10))
print(g)
for n in g:
    print(n, end=" ")
print()


# 第二种方法，使用函数实现列表生成式——斐波拉契数
# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b, end=" ") #函数的表达
        yield b  # 产生式的表达,yield 相当于断点
        a, b = b, a + b
        n = n + 1
    return 'done'


'''
这里，最难理解的就是generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，
遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''
# 调用该generator时，首先要生成一个generator对象
f = fib(6)
print(f)
for n in f:
    print(n, end=' ')

print()
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
from collections import Iterator

print(isinstance((x for x in range(10)), Iterator))

''''
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数：
'''
print(isinstance('abc', Iterator))  # false
print(isinstance(iter('abc'), Iterator))  # true

# 高阶函数：把一个函数名做另一个函数的参数
print(abs)  # <built-in function abs>
# 变量可以指向函数
f = abs
print(f(-10))  # 等价于 abs(-10)


# 函数名其实就是指向函数的变量

# 高阶函数
def add(x, y, f):
    return f(x) + f(y)


print(add(5, -10, abs))


# Python内建了map()和reduce()函数
def f(x):
    return x * x


r = map(f, [x for x in range(10)])
# Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(r))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(r)  # <map object at 0x7f9b71060f28>
print(list(map(str, [1, 2, 3, 4, 5])))

''''
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''

from functools import reduce


# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# 把str转换为int的函数
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def str2num(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(reduce(fn, map(char2num, '13579')))


# print(reduce(str2num, "13579"))


# 计算素数的一个方法是埃氏筛法

# 1. 定义一个生成器，生成无限序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 2. 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 3. 最后，定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 初始化序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible, it)  # 构造新序列


# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n, end=",")
    else:
        break

print()


# 闭包：相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())
# 装饰器:在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）,
# decorator就是一个返回函数的高阶函数

# 在now()函数调用前后自动打印日志
import datetime


# 构造装饰器
def log(func):
    def wrapper(*args, **kwargs):
        print('cal %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


'''
wrapper()函数的参数定义是(*args, **kw)，
因此，wrapper()函数可以接受任意参数的调用。
在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
'''


@log  # 调用装饰器
def now():
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(nowtime)


now()

'''
如果decorator本身需要传入参数，
那就需要编写一个返回decorator的高阶函数，
写出来会更复杂。比如，要自定义log的文本：
'''


def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("{0} {1}:".format(text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log('execute')
def now():
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(nowtime)


now()
print('now.__name__ = '+now.__name__)   #now.__name__ = wrapper
# 一个完整的decorator的写法如下：
import functools


def log(func):
    @functools.wraps(func)  #wrapper.__name__ = func.__name__
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(nowtime)


now()
print('now.__name__ = '+now.__name__)   #now.__name__ = wrapper
