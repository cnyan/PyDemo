#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-14 下午3:38
# @Author  : 闫继龙
# @File    : Student.py
# @Software: PyCharm

class Student(object):
    def __init__(self, name, score):
        self.name = name
        # 属性名如果以__开头，就变成了一个私有变量（private）
        self.__score = score

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。
    def print_score(self):
        print('%s:%s' % (self.name, self.__score))

    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

bart = Student('Bart simpson', 59)
lisa = Student('Lisa simpson', 89)
bart.print_score()
lisa.print_score()
print(type(bart))
print(bart)
bart.name = 'new Bart'
bart.print_score()

'''
双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
不能直接访问__name是因为Python解释器对外把__score变量改成了_Student__score，
所以，仍然可以通过_Student__score来访问__score变量：
'''
print(bart._Student__score)

bart.birth = 100
print(bart.birth)


