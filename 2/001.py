#!/usr/bin/python3
# -*- coding:utf-8 -*-



a = {1: [1, 2, 3]}
b = a.copy()
print(a, b)
a[1].append(4)
print(a, b)

import copy

c = copy.deepcopy(a)
print(a, c)
a[1].append(5)
print(a, c)
