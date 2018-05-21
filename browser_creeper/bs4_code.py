#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-21 下午4:20
# @Author  : 闫继龙
# @File    : bs4_code.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup(open('test.html'))
#print(soup.prettify())

# 获取html 里 title 的tag
print(type(soup.title))
print(soup.title.name)
print(soup.title)

# 获取标签里的文本(字符类型) string
print(soup.title.string)

# 获取 html 文件 <a> 标签的注释 comment
print(type(soup.a.string))
print(soup.a.string)

# 遍历所有元素
for item in soup.body.contents:
    print(item.name)


# css查询
print(soup.select('.coffe'))        #类
print(soup.select('#lin1'))         #id
print(soup.select('head > title'))    #层级关系