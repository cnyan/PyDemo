#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-14 下午8:59
# @Author  : 闫继龙
# @File    : json_text.py
# @Software: PyCharm

import json

'''
dumps()方法返回一个str，内容就是标准的JSON。
类似的，dump()方法可以直接把JSON写入一个file-like Object。
'''
dict = {'name': 'BOb', 'age': 20, 'score': 88}
print(json.dumps(dict))
print(type(json.dumps(dict)))
with open('/home/yan/temp/dump.txt', mode='w') as f:
    json.dump(dict, f)

'''
要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
'''
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
print(type(json.loads(json_str)))
with open('/home/yan/temp/dump.txt', mode='r') as f:
    dict = json.load(f)
print(dict)

print('----------class 直接序列化为 json-------------')

import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob class', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
s = json.loads(json_str)
print(s)


#re模块  正则表达式
import  re
result = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(result)