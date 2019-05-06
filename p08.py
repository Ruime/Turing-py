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
'''

print(int("12345", base=8))

# 新建一个函数，此函数是默认输入的字符串是16进制的数字
# 把此字符串返回十进制的数字
def int16(x, base=16):
    return int(x,base)
# print(int16("12345"))

import functools
int16 = functools.partial(int,base=16)
print(int16("123456"))





















