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