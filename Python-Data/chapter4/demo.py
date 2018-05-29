#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-28 下午2:24
# @Author  : 闫继龙
# @File    : demo.py
# @Software: PyCharm

'''
以纯Ｐython的形式实现　随机漫步

'''
import random

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) > 0 else -1
    position += step
    walk.append(position)

import numpy as np

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))  # 0或１
steps = np.where(draws>0,1,-1)
walks = steps.cumsum(axis=1) #cumsum 按轴累加
print(walks)

print(walks.max)
print(walks.max())