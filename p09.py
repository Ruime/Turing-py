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
'''
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