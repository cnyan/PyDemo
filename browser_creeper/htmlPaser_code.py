#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-21 下午5:03
# @Author  : 闫继龙
# @File    : htmlPaser_code.py
# @Software: PyCharm

from html.parser import HTMLParser


class MyHtmlParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)  # 你继承了HTMLParser，也要初始化父类的构造方法：


    def handle_decl(self, decl):
        HTMLParser.handle_decl(self, decl)
        print('decl %s ' % decl)

    def handle_starttag(self, tag, attrs):
        HTMLParser.handle_starttag(set, tag, attrs)
        print('<' + tag + '>')

    def handle_endtag(self, tag):
        HTMLParser.handle_endtag(self, tag)
        print('</' + tag + '>')

    def handle_data(self, data):
        HTMLParser.handle_data(self, data)
        print('data is ... %s ' % data)

    # <br/>
    def handle_startendtag(self, tag, attrs):
        HTMLParser.handle_startendtag(self, tag, attrs)

    def handle_comment(self, data):
        HTMLParser.handle_comment(self, data)
        print('data %s ' % data)

    def close(self):
        HTMLParser.close(self)
        print('Close')


myParser = MyHtmlParser()
myParser.feed(open('test.html').read())
myParser.close()
