#!/usr/bin/python3
# -*- coding:utf-8 -*-

# 常用内建模块

# datetime模块

# 获取当前日期和时间
from datetime import datetime

now = datetime.now()
print(now)  # 2017-10-17 16:15:30.839127
# 获取指定时间
dt = datetime(year=2017, month=10, day=17, hour=16, minute=17)
print(dt)  # 2017-10-17 16:17:00

# 时间戳转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))  # 2015-04-19 12:20:00    UTC时间

# str转换为datetime
cday = datetime.strptime('2017-10-17 16:20:20', '%Y-%m-%d %H:%M:%S')
print(cday)  # 2017-10-17 16:20:20

# datetime转换为str
print(now.strptime('%a,%b %d %H:%M'))  # Tue,Oct 17 16:22


# collections模块      集合类

'''
namedtuple是一个函数，
它用来创建一个自定义的tuple对象，
并且规定了tuple元素的个数，
并可以用属性而不是索引来引用tuple的某个元素
'''
# 用namedtuple写坐标函数
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # 1,2

'''
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
'''
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)  # deque(['y', 'a', 'b', 'c', 'x'])

'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。
如果希望key不存在时，返回一个默认值,使用defaultdict
'''
from collections import defaultdict

dd = defaultdict(lambda: '123')
dd['key1'] = 'abc'
print(dd['key1'], dd['key2'])  # abc  123

'''
使用dict时，Key是无序的。
在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict
'''
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

'''
Counter是一个简单的计数器，例如，统计字符出现的个数
'''
from collections import Counter

count = Counter()
for i in 'hello':
    count[i] += 1
print(count)  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
