#!/usr/bin/python3
# -*- coding:utf-8 -*-

# map(function,iterable) map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# 将列表里面的每个元素转换成字符串类型
ls = [1, 2, 3]
rs = map(str, ls)
print(list(rs))

# reduce(function,seq,inital)    需要from functools import  reduce
# 将序列[1,3,5,7,9]变为13579
from functools import reduce


def fun(x, y):
    return x * 10 + y


print(reduce(fun, [1, 3, 5, 7, 9]))

# 写一个str2float的函数
from functools import reduce


def str2float(s):
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

    def num2float(x, y):
        return x * 10 + y

    l = s.split('.')
    l1 = reduce(num2float, list(map(char2num, l[0])))
    l2 = reduce(num2float, list(map(char2num, l[1]))) / 10 ** len(l[1])
    return l1 + l2


print('str2float(\'123.456\') =', str2float('123.456'))

# filter(function,iterable)   ilter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

# 用埃氏筛法，计算质数
'''
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
不断筛下去，就可以得到所有的素数。
'''


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 100:
        print(n)
    else:
        break


# 利用filter()求回数，   回数：12321,909
def is_palindrome(n):
    return str(n) == str(n)[::-1]


output = filter(is_palindrome, range(1, 100))
print(output)

# sorter(iterable,key,reverse)   排序函数
list = [36, 5, -12, 9, -21]
print(sorted(list))  # [-21, -12, 5, 9, 36]
print(sorted(list, key=abs))  # [5, 9, -12, -21, 36]
print(sorted(list, reverse=True))  # [36, 9, 5, -12, -21]

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 分别按姓名排序 和分数排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def byName(t):
    return t[0]


def byScore(t):
    return t[1]


L2 = sorted(L, key=byName)
print(L2)
L3 = sorted(L, key=byScore)
print(L3)

# 装饰器        以下例子是一个标准装饰器
from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + 'was called')
        return func(*args, **kwargs)

    return with_logging

@logged
def f(x):
    '''do some math'''
    return x + x * x
print(f.__name__)
print(f.__doc__)


#偏函数

#利用int做进制转换
print((int('10')))          #10进制
print((int('10',base=8)))   #8进制
print((int('10',16)))       #16进制

#利用偏函数定义一个2进制转换
import functools
int2=functools.partial(int,base=2)
print(int2('10'))       #2

'''
简单总结functools.partial的作用就是，
把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单
'''

