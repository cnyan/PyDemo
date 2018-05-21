#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-19 下午8:27
# @Author  : 闫继龙
# @File    : 17huo_code.py
# @Software: PyCharm

import time
from selenium import webdriver
import numpy as np

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)

# 1. 网站有多少页商品（http://www.17huo.com/newsearch/?k=大衣）
browser.get('http://www.17huo.com/newsearch/?k=%E5%A4%A7%E4%B8%80')
page_info = browser.find_element_by_css_selector(
    'body > div.wrap > div.search_container > div.pagem.product_list_pager > div')

# 2. 共 3 页，每页 60 条
pages = int((page_info.text.split(', ')[0]).split(' ')[1])
print('商品共有%d 页' % pages)

# 3. 抓取每一页的数据
for i in range(pages):
    print('第 %d 页' % (i + 1))
    url = 'http://www.17huo.com/newsearch/?k=%E5%A4%A7%E4%B8%80&page' + str(i + 1)
    browser.get(url)
    # 模拟页面滚动，加载动态数据
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(3)
    # 抓取页面全部商品
    goods = browser.find_element_by_css_selector(
        'body > div.wrap > div.search_container > div.book-item-list.clearfix').find_elements_by_class_name(
        'book-item-list-box')
    print('第 %d 页,有 %d 件商品' % ((i + 1), len(goods)))

    # 4. 打印每件商品
    for i in np.arange(len(goods)):
        good = goods[i]

        try:
            title = good.find_element_by_css_selector('a > div.book-item-mid.clearfix > div.book-item-title').text
            price = good.find_element_by_css_selector('a > div.book-item-mid.clearfix > div.book-item-price > span').text
            print('商品序号：%d,  商品名称:%s,  商品价格：%s' % (i,title, price))
        except:
            print(good.text)
