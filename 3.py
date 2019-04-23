'''
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


'''


# 菱形继承问题
class A():
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
