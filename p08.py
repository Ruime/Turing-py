# <<<<<<< HEAD
from functools import reduce
# 计算一个数字的100倍
# 因为就是一个表达式，所以没有return
'''
stm = lambda x: 100 * x
print(stm(89))
stm1 = lambda x,y,z: x + y * 10 + z * 100
print(stm1(4,5,6))


# 变量可以赋值
# 函数名就是给一个变量

def funcA():
    print("In funcA")

funcB = funcA

funcB()


# # funcA是普通参数，返回一个传入数字的100倍的数字
def funcA(n):
    return n * 100
# # 把funcA传入的参数乘以3倍
# def funcB(n):
#     return funcA(n) * 3

# print(funcB(2))

def funcC(n, f):
    return f(n)*3

print((funcC(9, funcA)))

# map 举例
# 有一个列表，想对列表中的每一个元素乘以10，并得到新的列表

l = [1,2,3,4,5,6,7,8,9]

# l1 = [l for l in range()]
l2 = []
for i in l:
    l2.append(i * 10)

# print(l2)

# 利用map实现
def mulTen(n):
    return n * 10

l3 = map(mulTen, l)
# map 是一个可迭代的结构，所以可以使用for遍历
for i in l3:
    print(i)
# 以下列表生成式为空，为什么？
l4 = [i for i in l3]
print(l4)
'''

# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x,y):
    return x + y
# 对于列表[1,2,3,4,5,6]执行myAdd的reduc操作

rst = reduce( myAdd, [1,2,3,4,5,6])
print(rst)
# =======
# filter 案例
# 对于一个列表，对其进行过滤，偶数组生成一个心列表
# 需要定义过滤函数
# 过滤函数要求有输入，返回布尔值
'''
def isEven(a):
    return a % 2 == 0
l = [543,5,326,6,54,1,543,5,161,546,7,6,73,654]
rst = filter(isEven, l)
# 返回的filter内容是一个可迭代对象
print(type(rst))
print(rst)
print([i for i in rst])

# 排序案例1
a = [12432,5432,653,76,42,5,7,35,143231]
al = sorted(a, reverse= True)
print(al)

# 排序案例2
a = [-32,4,2,55,3,-245,3]
# 按照绝对值进行排序
# abs是求绝对值的意思
# 即按照绝对值的倒序排列
al = sorted(a, key=abs)
al1 = sorted(a, key=abs, reverse=True)
print(al)
print(al1)

# sorted案例
astr = ['a', 'k', 'c', 'd', 'e', 'f']

str = sorted(astr)
print(str)

# str1 = sorted(astr, key=str.)
# print(str1)

# 定义一个普通函数

def myF(a):
    print('In myF')
    return None

a = myF(4)
print(a)
# 函数作为返回值返回，被返回的函数在函数体内定义
def myF2():
    def myF3():
        print('In myF3')
        return 3
    return myF3
# 使用上面的定义
# 调用myF2,返回一个函数myF3，赋值给F3
f3 = myF2()
print(type(f3))
print(f3)



# 1.myf4 定义函数，返回内部定义函数myf5
# 2.myf5 使用了外部变量，这个变量是myf4的参数

def myF4(*args):

    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst

    return myF5


f5 = myF4(1, 2, 3, 4, 5, 6)
# f5的调用方式
f5()

# 装饰器(Decrator)
import time

# 打印hello word前打印系统时间，实现这个功能不能改变现有代码
# 使用装饰器
# 高阶函数，以函数作为参数
import time
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time:", time.ctime())
        return f(*args, **kwargs)
    return wrapper

# 上面定义了一个装饰器，使用时需要用到@，此符号是python的语法糖
# @printTime
# def Hello():
#     print("Hello word")

# Hello()


# 装饰器的好处是，一旦定义，则可以装饰任意函数
# 一旦被其装饰，则把装饰器的功能直接添加到定义函数的功能上
@printTime
def hello1():
    print("今天很高兴，被老板揪着讲课了")
    print("还可以有很多的选择")

hello1()

# 上面对函数的装饰使用了系统定义的语法糖
# 下面开始手动执行下装饰器
# 先定义函数
import time
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time:", time.ctime())
        return f(*args, **kwargs)
    return wrapper

def hello3():
    print("我是手动执行的")

hello3 = printTime(hello3)
hello3()

print(int("12345", base=8))

# 新建一个函数，此函数是默认输入的字符串是16进制的数字
# 把此字符串返回十进制的数字
def int16(x, base=16):
    return int(x,base)
# print(int16("12345"))

import functools
int16 = functools.partial(int,base=16)
print(int16("123456"))

# zip案例
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]
z = zip(l1,l2)
print(type(z))
print(z)
for i in z:
    print(i)

l1 = ["xiaowang", "xiaoli", "xiaohei"]
l2 = [89,23,99]
z = zip(l1,l2)
for i in z:
    print(i)

l3 = [i for i in z]
print(l3)

# enumerate
l1 = [11,22,33,44,55]

em = enumerate(l1)
l2 = [ i for i in em]
print(l2)
eu = enumerate(l1, start=100)
l2 = [ i for i in eu]
print(l2)

import collections
point = collections.namedtuple("point", ['x', 'y'])
p = point(11,22)
print(p.x)
print(p[0])


Circle = collections.namedtuple("Circle", ['x','y','r'])
c = Circle(100, 120, 20)
print(c)
print(type(c))
# 检测以下nametuple属于谁的子类
print(isinstance(c,tuple))


# dequeue

from collections import deque

q = deque(['a', 'b', 'c'])
print(q)

q.append('d')
print(q)

q.appendleft('x')
print(q)

# defaultdict
d1 = {"one":1, 'two':2,"three":3}
print(d1['one'])


from collections import defaultdict
func = lambda : 'rui'
d2 = defaultdict(func)
d2['one'] = 1
d2['two'] = 2
print(d2['one'])
print(d2['four'])
'''
# Counter
from collections import Counter

# 为什么下面结果不把abcdefg作为键值，而是其中每一个字母作为键值
# 需要括号里面的内容可迭代
c = Counter("abcdefg")
print(c)


















