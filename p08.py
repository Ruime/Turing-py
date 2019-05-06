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
'''


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