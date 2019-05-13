import pickle
import shelve
# 打开文件，用写的方式
# f 称之为文件句柄
# r 表示文件后面的字符串内容不需要转义
'''
f = open(r"test01.txt", "w")
# 文件打开后必须关闭
f.close()
# 此案例说明，以写方式打开文件默认是如果没有文件，则创建

# with语句案例

with open(r"test01.txt", "r") as f:
    pass
    # 下面语句块开始对文件F进行操作
    # 在本模块中不需要使用close关闭文件f

# with案例

# with open(r"test01.txt","r") as f:
#     # 按行读取内容
#     strline = f.readline()
#     # 此结构保证能够完整读取文件知道结束
#     while strline:
#         print(strline)
#         strline = f.readline()
with open('test01.txt', 'r',encoding='utf-8') as f:
    # 按行读取内容
    line = f.readline()
    # 此结构保证能够完整读取文件知道结束
    while line:
        print(line)
        line = f.readline()


# list能用打开文件作为参数，把文件内每一行内容作为一个元素
with open(r"test01.txt","r", encoding='utf-8') as f:
    # 以打开的文件f作为参数，创建列表
    l = list(f)
    for line in l:
        print(line)

# read是按字符读取文件内容
# 允许输入参数决定读取几个字符，如果没有指定，从当前位置内容读取到结尾
# 否则，从当前位置读取当前位置读取指定的几个数字符
with open(r"test01.txt", "r", encoding='utf-8') as f:
    strChar = f.read(1)
    while strChar:
        print(strChar)
        strChar = f.readline()
    # print(len(strChar))
    # print(strChar)
# 作业：
# 使用read读文件，每次读一个，实用循环读完
# 尽量保持格式

# seek(offset,from)案例
# 打开文件后，从第五个字节开始读取
# 打开读写指针在0处，即文件的开头
with open(r"test01.txt", "r", encoding='utf-8') as f:
    # seek移动单位是字节
    f.seek(0, 0)
    strChar = f.read()
    print(strChar)

# 关于读取文件的练习
# 打开文件，三个字符一组读出内容，打印
# 每读一次，休息一秒

import time
with open(r"test01.txt", "r", encoding='utf-8') as f:
    # read参数的单位是字符，可以理解为一个汉字就是一个字符
    strChar = f.read(3)
    while strChar:
        print(strChar)
        time.sleep(1)
        strChar = f.read(3)

# tell 函数：用来显示文件读写指针当前的位置
with open(r"test01.txt", "r", encoding='utf-8') as f:
    strChar = f.read(3)
    pos = f.tell()

    while strChar:
        print(pos)
        print(strChar)
        strChar = f.read(3)
        pos = f.tell()
# 以下结果说明：
# tell的返回数字的单位是byte
# read是以字符为单位

# write 案例
# 1.向文件追加一句诗
with open(r"test01.txt", "a") as f:
    f.write("\n我曾想要我的歌声\n\n无尽沉沦的感动")

# 可以直接写入行,用writeline
# a代表追加方式打开
with open(r"test01.txt", "a") as f:
    f.writelines("\n我曾想要我的歌声")
    f.writelines("\n\n无尽沉沦的感动")

l = ["I", "love", "python"]
with open(r"test01.txt", "w") as f:
    f.writelines(l)
# 序列化案例
age = 18
with open(r"test01.txt", "wb") as f:
    pickle.dump(age, f)

# 反序列化案例
with open(r"test01.txt", "rb") as f:
    age = pickle.load(f)
    print(age)

# 使用shelve创建文件并使用
# 打开文件
# shv相当与一个字典
shv = shelve.open(r"shv.db")

shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()

# 通过以上案例发现，shelve自动创建的不仅仅是一个shv,db文件，还包括其它格式的文件
# shelve读取案例
shv = shelve.open(r'shv.db')

try:
    print(shv['one'])
    print(shv['three'])
finally:
    shv.close()


# shelve 之只读打开
shv = shelve.open(r'shv.db', flag='r')

try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()



shv = shelve.open(r'shv.db')
try:
    shv['one'] = {"eins":1, "zwei":2, "drei":3}
finally:
    shv.close()


shv = shelve.open(r'shv.db')
try:
    one = shv['one']
    print(one)
finally:
    shv.close()

# shelve忘记写回，需要使用强制写回
shv = shelve.open(r'shv.db', writeback=True)
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是在内存中，没有写回数据库
    k1["eins"] = 100
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
    k1["eins"] = 100
finally:
    shv.close()
'''
# shelve 使用with管理上下文环境
with shelve.open(r'shv.db', writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] =1000

with shelve.open(r'shv.db') as shv:
    print(shv['one'])




















