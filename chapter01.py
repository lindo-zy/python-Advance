#!/usr/bin/python3
# -*- coding:utf-8 -*-

# python3 命名关键字参数

def person(name, *, age, num):  # *后面的为必须传入的同名参数
    print(name, age, num)


person('Alice', age='12', num='123')


# python3递归函数

# 计算阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


'''
存在调用递归次数多，栈溢出的情况
'''


# 改进后，尾递归方式
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


'''
不过python解释器并没有对尾递归也进行优化，所以还是存在栈溢出，少用递归
'''

# 列表生成器
'''
生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
list(range(1, 11))

'''
生成[1x1, 2x2, 3x3, ..., 10x10]
'''
list = [x * x for x in range(1, 11)]

'''
生成仅有偶数的列表
'''
list = [x * x for x in range(1, 11) if x % 2 == 0]

'''
生成全排列的列表
'''
list = [m + n for m in 'ABC' for n in 'XYZ']

#python3 生成器
#生成一个杨辉三角      [1,2,1]=[1,1,0]+[0,1,1]
def triangles():
    T = [1]
    while True:
        yield T
        T = [(T + [0])[i] + ([0] + T)[i] for i in range(len(T + [0]))]
        # L = [1] + [L[i - 1] + L[i] for i in range(len(L)) if i > 0] + [1]
        print(T)
n = 0
for i in triangles():
    n += 1
    if n == 10:
        break


