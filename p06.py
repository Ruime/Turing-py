'''
# 简单异常案例
try:
    num = int(input("Plz input your number"))
    rst = 100/num
    print("计算结果是{0}".format(rst))
except:
    print("输了内容有误")
    exit()

# 简单异常案例
# 给出提示信息
try:
    num = int(input("Plz input your number"))
    rst = 100/num
    print("计算结果是{0}".format(rst))
# 捕获异常后，把异常实例化，出错信息在实例化里
# 注意以下写法
# 以下语句是捕获ZeroDivisionError异常并实例化实例e
except ZeroDivisionError as e:
    print("输了内容有误")
    print(e)
    exit()

# 简单异常案例
# 给出提示信息
try:
    num = int(input("Plz input your number"))
    rst = 100/num
    print("计算结果是{0}".format(rst))
# 如果是多种error的情况
# 需要把越具体的错误越往前放
# 在异常类继承关系中，越是子类的异常，越要往前放
# 越是父类的异常，越要往后放

# 在处理异常的时候，一旦拦截到某一个异常，则不再往下查看，直接进行下一个
# 代码，即有finally则执行finally语句块，否则就执行下一个打的语句
except ZeroDivisionError as e:
    print("输了内容有误")
    print(e)
    exit()
except NameError as e:
    print("名字起错了")
    print(e)
    exit()
except AttributeError as e:
    print("好像属性有问题")
    print(e)
    exit()
# 所有异常都是继承自Exception
# 如果写上下面这句话，任何异常都会拦截住
# 而且，下面这句话一定是最后一个exception
except Exception as e:
    print("不知道哪儿出错")
    print(e)
    exit()

# raise案例
try:
    print("俺是熊大")
    print(3.1415926)
    # 手动引发一个异常
    # 注意语法：raise errorclassname
    raise ValueError
    print("还没完啊")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会被执行的")

# raise案例-2
# 自己定义异常
# 需要注意：自定义异常必须是子异常的子类
class RuiValueError(ValueError):
    pass
try:
    print("俺是熊大")
    print(3.1415926)
    # 手动引发一个异常
    # 注意语法：raise errorclassname
    raise RuiValueError
    print("还没完啊")
except NameError as e:
    print("NameError")
# except RuiValueError as e:
#     print("RuiValueError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会被执行的")

# else语句案例
try:
    num = int(input("Plz input your number"))
    rst = 100 / num
    print("计算结果是{0}".format(rst))
except Exception as e:
    print("Exception")
else:
    print("No Exception")
finally:
    print("反正我会被执行的")
'''
