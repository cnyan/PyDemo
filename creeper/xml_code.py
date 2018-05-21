#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-19 下午7:15
# @Author  : 闫继龙
# @File    : xml_code.py
# @Software: PyCharm

print('方法一：使用dom 解析xml')

from xml.dom import minidom

doc = minidom.parse('book.xml')
root = doc.documentElement

print(type(root))
print(dir(root))
print(root.nodeName)

books = root.getElementsByTagName('book')
for book in books:
    titles = book.getElementsByTagName('title')
    prices = book.getElementsByTagName('price')

    title = titles[0].childNodes[0].nodeValue
    price = prices[0].childNodes[0].nodeValue

    print(title, price)

print('----------------------分割线----------------------')

print('方法二，使用 sax 解析xml')
import string
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def __init__(self):
        pass

    def start_element(self, name, attrs):
        self.name = name
        print('element: %s,attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('end element:%s' % name)

    def char_data(self, text):
        if text.strip():
            print('%s text is: %s ' % (self.name, text))


handler = DefaultSaxHandler()
parser = ParserCreate()

parser.StartElementHandler = handler.start_element  # <book>
parser.EndElementHandler = handler.end_element  # </book>
parser.CharacterDataHandler = handler.char_data  # <title>learn python</title> 处理文本

with open('book.xml', 'r') as f:
    parser.Parse(f.read())
