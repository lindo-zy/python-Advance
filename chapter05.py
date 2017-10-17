#!/usr/bin/python3
# -*- coding:utf-8 -*-


# hashlib    提供摘要算法

# 利用hashlib计算MD5
import hashlib

md5 = hashlib.md5()
md5.update('passwd'.encode('utf-8'))
print(md5.hexdigest())  # 76a2173be6393254e72ffa4d6df1030a

# itertools  提供用于操作迭代对象的函数
'''
无限迭代器
'''
import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)  # 无限输出自然数

cs = itertools.cycle('AB')
for n in cs:
    print(n)  # 无限输出'A','B'，'A','B'

ns = itertools.repeat('A', times=3)
for n in ns:
    print(n)  # 输出‘A','A','A'

'''
迭代操作函数
'''
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('AB', 'XY'):
    print(c)  # A B X Y

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AABBBCCAAA'):
    print(key, list(group))
# 结果如下
'''
A ['A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']
'''
for key, group in itertools.groupby('AaaBBbcCCAAa', lambda c: c.upper()):
    print(key, list(group))
# 结果如下
'''
A ['A', 'a', 'a']
B ['B', 'B', 'b']
C ['c', 'C']
A ['A', 'A', 'a']
'''


