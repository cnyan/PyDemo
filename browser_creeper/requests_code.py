#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-21 下午2:28
# @Author  : 闫继龙
# @File    : requests_code.py
# @Software: PyCharm

import requests
from PIL import Image
from io import BytesIO
import json

print(dir(requests))

# URL get请求
url = 'http://www.baidu.com'
r = requests.get(url)
print(r.text)  # 文本数据
print(r.status_code)
print(r.encoding)
print(r.content)  # 二进制数据

'''
print('=========分隔符=============== \n')
# 传递参数：
parmas = {'k1': 'k1', 'k2': 'k2'}
r = requests.get('http://httpbin.org/get', parmas)
print(r.url)
'''

print('=========分隔符=============== \n')
# 二进制图片处理
url = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1136395033,781729131&fm=27&gp=0.jpg'
response = requests.get(url)
image = Image.open(BytesIO(response.content))
image.save('../src/moon.jpg')

print('=========分隔符=============== \n')
# json处理
response = requests.get('https://github.com/timeline.json')
print(type(response))
print(response.json())
print(response.json)
print(response.text)

print('=========分隔符=============== \n')
# 原始数据处理
url = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1136395033,781729131&fm=27&gp=0.jpg'
response = requests.get(url, stream=True)
with open('../src/moon2.jpg', 'wb+') as f:
    for chunk in response.iter_content(1024):
        f.write(chunk)

print('=========分隔符=============== \n')
# 提交表单
form = {'username': 'user', 'password': 'pass'}
response = requests.post('http://httpbin.org/post', data=form)
print(response.text)

response = requests.post('http://httpbin.org/post', data=json.dumps(form))
print(response.text)

print('=========分隔符=============== \n')
# 遍历cookies
response = requests.get('https://www.baidu.com')
cookies = response.cookies
for k, v in cookies.get_dict().items():
    print(k + ' ----- ' + v)

print('=========分隔符=============== \n')
# 发送请求时，带入cookies信息
cookies = {'c1': 'v1', 'c2': 'v2'}
response = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(response.text)

print('=========分隔符=============== \n')
# 重定向和重定向历史

response = requests.head('http://github.com',allow_redirects=True)
print(response.url)
print(response.status_code)
print(response.history)

print('=========分隔符=============== \n')
