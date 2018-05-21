#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-18 下午6:42
# @Author  : 闫继龙
# @File    : post_code.py
# @Software: PyCharm

import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.__provinces = provinces

    # 处理标签开始
    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.__provinces.append((name, number))

    # 处理标签结束
    def end_element(self, name):
        pass

    # 文本处理
    def char_data(self, text):
        pass

    @property
    def provinces(self):
        return self.__provinces

    @provinces.setter
    def provinces(self, value):
        self.__provinces = value


def get_province_entry(url):
    # 获取文本，并用 gb2312编码
    content = requests.get(url).content.decode('gb2312')
    # print(content)
    start = content.find('<map name="map_86" id="map_86">')
    end = content.find('</map>')
    # 获取切片内容
    content = content[start:end + len('</map>')].strip()

    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(content)

    provinces = []
    # 解读XML 文件
    handler = DefaultSaxHandler(provinces)
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(content)

    return provinces


province = get_province_entry('http://www.ip138.com/post')
print(province)
