# 0. oop-python 面向对象
- python的面向对象
- 面向对象编程
    - 基础
    - 共有私有
    - 继承
    - 组合、Mixin
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
    
# 1. 面向对象概述(ObjectOriented,OO)
- OO思想
    - 接触到任意一个任务，首先想到的是这个世界的构成，是由模型构成的
- 名词
    - OO：面向对象
    - OOA：面向对象的分析
    - OOD：面向对象的设计
    - OOI：XXX的实现
    - OOP：XXX的编程
    - OOA->OOD->OOI:面向对象实现的过程
- 类的对象和概念
    - 类：抽象名词，代表一个集合，共性的事物
    - 对象：具像的事物，单个个体
    - 类跟对象的关系
        - 一个具象，代表一类事物的某一个个体
        - 一个是抽象，代表的是一大类事物
- 类中的内容，应该具有两个内容
    - 表明事物的特征，叫做属性(变量)
    - 表明事物功能或动作，称为成员变量法(函数)
    
# 2. 类的基本实现
- 类的命名
    - 遵守变量命名的规范
    - 大驼峰(由一个或者多个单词构成，每个单词首字母大写，单词跟单词直接相连)
    - 尽量避开跟系统命名相似的命名
- 如何声明一个类
    - 必须用Class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，可以使用None
    - 案例01.py
- 实例化类

        变量 = 类名()#实例化了一个对象
        
- 访问对象成员
    - 使用点操作符号
        
        obj.成员属性名称
        obj.成员方法
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所称成员检查
        # dict前后各有两个下划线
        obj.__dict__
        
    - 类所有的成员
    
        # dict前后各有两个下划线
        class_name.__dict__
# 3. anaconda基本使用
- anaconda主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda常用命令：
    - conda deactivate(退出当前环境)
    - conda remove -n name(删除名为name的环境)
    - conda create -n OOP python3.6(创建py版本为3.6,名为OOP的环境)
    - source activate OOP(激活名为OOP的环境)
    - conda activate OOP(进入OOP虚拟环境)
    - conda list : 显示anaconda的安装包
    - conda env list：显示anaconda的虚拟环境

# 4. 类和对象的成员分析
- 类和对象都可以存储成员，成员归类所有
- 类存储成员时使用的是与类关联的一个对象
- 独享存储成员是存储在当前对象中
- 对象访问一个成员时，如果对象中没有改成员，尝试访问类中的同名成员，如果对象中有此成员，一定使用对象中的成员
- 创建对象的时候，类中的成员不会放入对象当中，而是得到一个空对象，没有成员
- 通过对象对类中成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员

# 5. 关于self
- self在对象中的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法中的第一个参数中

### 关于self
    class Student():
        name = 'rui'
        age = 18
    
        #注意say的写法，参数由一个self
        def say(self):
            self.name = 'aaa'
            self.age = 20
            print('My name is {0}'.format(self.name))
            print("My age is {0}".format(self.age))
    xiaoma = Student()
    xiaoma.say()

    class Student():
        name = 'rui'
        age = 18
        #注意say的写法，参数由一个self
        def sayAgain(s):
            s.name = 'aaa'
            s.age = 20
            print('My name is {0}'.format(s.name))
            print("My age is {0}".format(s.age))
    
    xiaoma = Student()
    xiaoma.sayAgain()
    
    # 结果：
    My name is aaa
    My age is 20
    My name is aaa
    My age is 20
- self并不是关键字，只是一个用于接收对象的普通参数，理论上可以用任何一个普通变量名代替
- 方法中有self形参的方法成为非绑定类的方法可以通过对象访问、没有self的是绑定类的方法，只能通过类访问
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__

### 案例
    class Teacher():
        name = 'rui'
        age = 18
    
        def say(self):
            self.name = 'aaa'
            self.age = 20
            print('My name is {0}'.format(self.name))
            # 调用类的成员变量需要使用__class__
            print("My age is {0}".format(__class__.age))
    
        def sayAgain(self):
            print(__class__.name)
            print(__class__.age)
            print("Hello, nice to see you again")
    t = Teacher()
    t.say()
    # 调用绑定类函数使用类名
    Teacher.sayAgain()

    class A(set):
    name = 'rui'
    age = 18

    def __init__(self):
        self.name = 'aaa'
        self.age = 20

    def say(self):
        print(self.name)
        print(self.age)


    class B(set):
        name = "bbb"
        age = 30
    
    a = A()
    # 此时，系统会默认把a最为第一个参数传入函数
    a.say()
    # 此时A为类实例,self被a替换
    A.say(a)
    # 同样可以把A作为参数传入
    A.say(A)
    # 此时，传入的是类实B，因为B具有name和age属性，所以不会报错
    A.say(B)
    
    # 结果：
    aaa
    20
    aaa
    20
    rui
    18
    bbb
    30
    
    # 以上代码利用了鸭子模型

# 6. 面向对象的三大特性
- 封装
- 继承
- 多态

# 6.1 封装
- 封装就是对对象成员进行访问限制
- 封装的三个级别
    - 公开. public
    - 受保护的. protected
    - 私有的. private
    - public. protected. private不是关键字
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
- 私有
    - 私有成员是最高级别的封装，只能在当前类或对象中访问
    - 在成员前面添加两个下划线即可

            class person():
                # name是共有的成员
                # __age就是私有成员
                __age = 18
                
    - python的私有不是真的私有，是一种成为name mangling的改名策略，可以使用对象._calssname_attributename访问

                class person():
                    # name是共有的成员
                    name = 'rui'
                    # __age就是私有成员
                    __age = 18

                p = person()
                # name 是共有变量
                print(p.name)
                # age 是私有变量
                # 注意报错信息
                # print(p.__age)

                # name mangling技术
                print(person.__dict__)
                p.__Person__age = 18
                print(p.__Person__age)
                
                # 结果：
                rui
                {'__module__': '__main__', 'name': 'rui', '_person__age': 18, '__dict__': <attribute '__dict__' of 'person' objects>, '__weakref__': <attribute '__weakref__' of 'person' objects>, '__doc__': None}
                18






