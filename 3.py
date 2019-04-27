
class A():
    pass


class B(A):
    pass

class C(B,A):
    pass

print(A.__mro__)
print(B.__mro__)


# 多继承的例子
# 子类可以直接拥有父类的属性和方法
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("I am swimming ... ...")

class Bird():
    def __init__(self,name):
        self.name = name

    def fly(self):
        print("I am flying......")

class Person():
    def __init__(self,name):
        self.name = name

    def work(self):
        print("Working......")


# 单继承的例子
class Student(Person):
    def __init__(self, name):
        self.name = name

stu = Student('xiaoma')
stu.work()

# 多继承的例子
class SuperMan(Person, Bird, Fish):
    def __init__(self,name):
        self.name = name


class SwimMan(Person, Fish):
    def __init__(self,name):
        self.name = name


s = SuperMan("xiaoma")
s.fly()
s.swim()


# 菱形继承问题
class A():
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


# 构造函数例子(魔法函数)
class Person():
    # 对Person类进行实例化的时候
    # 姓名要确定
    # 年龄要确定
    # 地址要确定
    pass

    def __init__(self):
        self.name = "no name"
        self.age = 18
        self.address = "宿舍"
        print("In init func")

# 实例化一个人
p =Person()


# 构造函数的调用顺序 -1
# 如果子类没有写构造函数，则自动向上查找，直到找到位置
class A():
    pass

class B(A):
    def __init__(self):
        print("B")


class C(B):
    pass

# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到为止

c = C()


# 构造函数的调用顺序 -2
# 如果子类没有写构造函数，则自动向上查找，直到找到位置
class A():
    def __init__(self):
        print("A")


class B(A):
    def __init__(self, name):
        print("B")
        print(name)


class C(B):
    pass

# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到为止
# 此时，会出现参数结构不对应错误，一定要与构造函数的参数相对应
c = C()




# 构造函数的调用顺序 -3
# 如果子类没有写构造函数，则自动向上查找，直到找到位置
class A():
    def __init__(self):
        print("A")


class B(A):
    def __init__(self, name):
        print("B")
        print(name)


class C(B):
    # c中想扩展B的构造函数
    # 即调用B的构造函数在后面添加一些功能
    # 有两种方法实现：

    ''''''
    # 第一种是通过父类名调用
    def __init__(self, name):
        # 首先调用父类构造函数
        B.__init__(self, name)
        # 其次，再增加自己的功能
        print("这是C中附加的功能")
    ''''''
    # 第二种，使用super调用
    def __init__(self, name):
        # 首先调用父类构造函数
        super(C, self).__init__(name)
        # 其次，再增加自己的功能
        print("这是C中附加的功能")
# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到为止
# 此时，会出现参数结构不对应错误，一定要与构造函数的参数相对应
c = C("我C")


# issubclass()
class A():
    pass
class B():
    pass
class C(A):
    pass


print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(B, object))

# isinstance()
class A():
    pass
a = A
print(isinstance(a, A))


# hasattr()
class A():
    name = "no name"

a = A()
print(hasattr(a, "name"))
print(hasattr(a, "age"))

# halp 案例

help(setattr)

# dir案例
class A():
    pass

print(dir(A))