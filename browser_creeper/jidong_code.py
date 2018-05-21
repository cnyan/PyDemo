#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-20 下午2:31
# @Author  : 闫继龙
# @File    : jidong_code.py
# @Software: PyCharm

from selenium import webdriver
import numpy as np
import time

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)

# 1.查看多少页面
browser.get(
    'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=8c843bd7216f4f6eaff661b402cb7b51')

pages_count = browser.find_element_by_css_selector('#J_bottomPage > span.p-skip > em:nth-child(1) > b')
pages = int(pages_count.text)
print('共有商品 %d 页' % pages)

# 2. 抓取每页数据
for i in range(5):
    print('当前第 %d 页' % (i + 1))
    url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=' \
          + str((1 + 2 * (i - 1))) + '&s=232&click=0'
    browser.get(url)

    # 模拟页面滚动，获取动态数据
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)

    goods = browser.find_element_by_css_selector('#J_goodsList > ul').find_elements_by_class_name('gl-item')
    print('第 %d 页,有 %d 件商品' % ((i + 1), len(goods)))

    # 获取每页每件商品信息
    for i in np.arange(len(goods)):
        good = goods[i]

        try:
            name = browser.find_element_by_css_selector(
                'li:nth-child(' + str(i + 1) + ') > div > div.p-name.p-name-type-2 > a > em').text
            price = browser.find_element_by_css_selector(
                'li:nth-child(' + str(i + 1) + ') > div > div.p-price > strong > i').text
            print('商品序号：%d,  商品名称:%s,  商品价格：%s' % (i, name, price))
        except:
            print(good.text)
