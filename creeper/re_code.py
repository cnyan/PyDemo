#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-19 下午7:55
# @Author  : 闫继龙
# @File    : re_code.py
# @Software: PyCharm

import re

# 3位数字-3到8个数字 \d{3}-\d{3-8}

rm = re.match(r'\d{3}-\d{3-8}', '010-223456')
print(rm.string)

# 分组
rm = re.match(r'(\d{3}-\d{3-8})$', '010-223456')
print(rm.groups())
print(rm.group(0))  # 原始字符串

