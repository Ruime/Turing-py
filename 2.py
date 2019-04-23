# 继承的语法
# 在python中任何一个类都有一个共同的父类叫object
'''

class Person():
    name = 'NoName'
    age = 0
    __score = 0 # 考试成绩，只能自己知道
    _petname = "sec"# 小名，是受保护的，子类可用，不能共用

    def sleep(self):
        print("Sleeping ... ...")


# 父类写在括号内
class Teacher(Person):
    teacher_id = '001'
    def make_test(self):
        print("attention")


t = Teacher()
print(t.name)
# 受保护不能外部访问，为什么这里可以访问
print(t._petname)
# 私有访问问题,结果报错，没有该属性
# print(t.__score)
t.sleep()

# 子类中独有的东西
print(t.teacher_id)
t.make_test()
'''



'''
# 子类和父类定义同一个名称变量，则优先使用子类本身
class Person():
    name = 'NoName'
    age = 0
    __score = 0 # 考试成绩，只能自己知道
    _petname = "sec" # 小名，是受保护的，子类可用，不能共用

    def sleep(self):
        print("Sleeping ... ...")


class Teacher(Person):
    teacher_id = '001'
    name = 'wang'
    def make_test(self):
        print("attention")


t = Teacher() # 子类和父类中成员如果相同，则优先使用子类成员
print(t.name)

'''

'''
# 子类扩充父类功能的案例
# 人有工作的函数，老师也有工作的函数，但老师的工作需要讲课
class Person():
    name = 'NoName'
    age = 0

    def work(self):
        print("make some money")


class Teacher(Person):
    teacher_id = '001'
    name = 'wang'

    def make_test(self):
        print("attention")

    def work(self):
        # 扩充父类功能只需要调用父类相同的函数
        # Person.work(self)
        # self.make_test()
        # 扩充父类的另一种方：super，代表得到父类
        super().work()
        self.make_test()


t = Teacher()
t.work()
'''

'''

# 构造函数的概念
class Dog():
    # __init__就是构造函数
    # 每次实例化的时候第一个被调用
    # 因为主要工作是进行初始化，所以得名构造函数(构造函数的第一个参数一定是self)
    def __init__(self):
        print("I am init in dog")
# 实例化的时候，括号内的参数需要跟构造函数参数匹配
benben = Dog()


# 继承中的构造函数
class Animel():
    pass


class PaxingAni(Animel):
    pass


class Dog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候第一个被调用
    # 因为主要工作是进行初始化，所以得名构造函数(构造函数的第一个参数一定是self)
    def __init__(self):
        print("I am init in dog")

# 实例化的时候自动调用了Dog的构造函数
benben = Dog()


# 继承中的构造函数 - 2
class Animel():
    def __init__(self):
        print("Animel")


class PaxingAni(Animel):

    def __init__(self):
        super().__init__()
        print("paxing dongwu")


class Dog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候第一个被调用
    # 因为主要工作是进行初始化，所以得名构造函数(构造函数的第一个参数一定是self)
    def __init__(self):
        print("I am init in dog")

# 实例化的时候自动调用了Dog的构造函数
# 因为对象找到类构造函数，则不再查找父类中的构造函数
benben = Dog()

# 猫没有写构造函数
class Cat(PaxingAni):
    pass

# 此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类的构造函数
# 在PaxingAin中查找了构造函数，则停止向上查找
c = Cat()


# 继承中的构造函数 - 3
class Animel():
    def __init__(self):
        print("Animel")


class PaxingAni(Animel):
    def __init__(self, name):
        print("paxing dongwu {0}".format(name))


class Dog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候第一个被调用
    # 因为主要工作是进行初始化，所以得名构造函数(构造函数的第一个参数一定是self)
    def __init__(self):
        print("I am init in dog")

d = Dog()


class Cat(PaxingAni):
    pass
# 此时，由于Cat没有构造函数，则向上查找
# 因为PaxingAni的构造函数需要两个参数，实例化的时候给了一个，报错
c = Cat()


# 继承中的构造函数 - 4
class Animel():
    def __init__(self):
        print("Animel")


class PaxingAni(Animel):
    pass


class Dog(PaxingAni):
    pass

d = Dog()


class Cat(PaxingAni):
    pass
# 此时，由于Cat没有构造函数，则向上查找
# 因为PaxingAni的构造函数需要两个参数，实例化的时候给了一个，报错
c = Cat()
# 结果：
# Animel
# Animel
'''





















