# 属性案例
# 创建Student类，描述学生类
# 学生具有Student, name属性
# 但name格式并不统一
# 可以用
'''
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 如果不想改代码
        self.setName(name)

    # 介绍
    def intro(self):
        print("Hi, my name is {0}".format(self.name))

    def setName(self, name):
        self.name = name.upper()

s1 = Student("RUI", 18)
s2 = Student("michi stangle", 24)
s1.intro()
s2.intro()

# property案例
# 定义一个Person类， 具有name, age属性
# 对于任意输入的姓名，我们希望都用大写保存
# 年龄，同意用整数保存
# x = property(fget, fset, fdel, doc)
class Person():
‘’‘’‘’
    测试
‘’‘’‘’
    # 函数名称可以任意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        # 所有输入的姓名以大写形式保存
        self._name = name.upper()

    def fdel(self):
        self._name = "No Name"

    name = property(fget, fset, fdel)
p1 = Person()
p1.name = "tt"
print(p1.name)



# 类的内置属性距离

print(Person.__dict__)
print(Person.__doc__)
print(Person.__bases__)

# init 举例
class A():
    def __init__(self, name = 0):
        print("哈哈，我被调用了")

a = A()

# __call__举例
class A():
    def __init__(self, name = 0):
        print("哈哈，我被调用了")

    def __call__(self):
        print("我被调用了again")
a = A()
a()

# __str__举例
class A():
    def __init__(self, name = 0):
        print("哈哈，我被调用了")

    def __call__(self):
        print("我被调用了again")

    def __str__(self):
        return "例子"
a = A()
print(a)

# __getattr__
class A():
    name = "Noname"
    age = 18

    def __getattr__(self, name):
        print("找不到该属性")
        print(name)

a = A()
print(a.name)
print(a.adder)

# __setattr__案例
class Person():
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        print("设置属性：{0}".format(name))
        # 下面语句会导致问题，死循环
        # self.name = value
        # 此情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name, value)
p = Person()
print(p.__dict__)

# __gt__举例

class Student():
    def __init__(self, name):
        self._name = name

    def __gt__(self, obj):
        print("哈哈， {0}会比{1}大吗？".format(self,obj))
        return self._name > obj._name

stu1 = Student("one")
stu2 = Student("two")
print(stu1 < stu2)


class Person:
    # 实例方法
    def eat(self):
        print(self)
        print("Eating......")

    # 类方法
    # 类方法的第一个参数，一般命名为cls,区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing......")

    # 静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("Saying......")

xiaoma = Person()

# 实例方法
xiaoma.eat()
# 类方法
Person.play()
xiaoma.play()
# 静态方法
Person.say()
xiaoma.say()



## 变量的三种用法

class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18

a = A()
# 属性的三种用法
# 1、赋值
# 2、读取
# 3、删除
a.name = "rui"
print(a.name)
del a.name
print(a.name)

# 类属性 prooerty
# 应用场景
# 对变量除了普通的三种操作，还想增加一些附加的操作，那么可以用property完成

class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18
    # 此功能，是对变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print("我被读取了")
        return self.name
    # 模拟的是对变量进行写操作的时候执行的功能
    def fset(self, name):
        print("我被写入了，但是还可以做好多事情")
        self.name = "rui name" + name
    # 模拟的是删除变量的时候进行的操作
    def fdel(self):
        pass
    # property的四个参数顺序是固定的
    # 第一个参数代表的是读取的时候需要调用的函数
    # 第二个参数代表写入的时候需要调用的函数
    # 第三个是删除
    name2 = property(fget, fset, fdel, "这是一个property的例子")

a = A()
a.name = "xiaoma"
print(a.name)

print(a.name2)

# 抽象
class Animel():
    pass

    # def sayHello(self):
        # pass
        # print("闻下对方的味道")

class Dog(Animel):
    pass
    # def sayHello(self):
    #     print("闻一下对方")

class Person():

    def sayHello(self):
        print("kiss me")

d = Dog()
d.sayHello()

p = Person()
p.sayHello()


# 抽象类的实现
import abc

# 声明一个类并且指定当前类的元素
class Human(metaclass=abc.ABCMeta):

    # 定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass
    # 定义类抽象方法
    @abc.abstractclassmethod
    def dirnk():
        pass
    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    def sleep(self):
        print("Sleeping...")


# 函数名可以当变量是使用
def sayHello(name):
    print("{0},您好".format(name))

# sayHello("老师")
ll = sayHello
ll ("老师")


# 自己组装一个类
class A():
    pass

def say(self):
    print("Saying......")


class B():
    def say(self):
        print("Saying......")
say(9)

A.say = say

a = A()
a.say()


# 利用type找一个类
# 先定义应该具有的成员函数
def say(self):
    print("Saying ......")

def talk(self):
    print("Talking ......")

'''


# 用type来创建一个类
def say(self):
    print("Saying......")


def talk(self):
    print("Talking......")


A = type("Aname", (object,), {"class_say": say, "class_talk": talk})

# 然后可以想正常访问一样使用类
a = A()
dir(a)


# 元类演示
# 元类写法是固定的，他必须继承自type


class TulingMetaClass(type):

    def __nwe__(cls, name, bases, attrs):
        print("俺是元类")
        attrs['id'] = '000000'
        attrs['addr'] = "北京市海淀区公主坟西翠路12号"
        return type.__new__(cls, name, bases, attrs)


# 元类定义完就可以用，使用注意写法


class Teacher(object, metaclass=TulingMetaClass):
    pass


t = Teacher()

# t.id
