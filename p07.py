import calendar
import time
import timeit
import datetime
from datetime import datetime,  timedelta
import os
import os.path as op
import zipfile
import random
'''
# 获取一年日历的字符串
# 参数
# w = 每个日期之间的间隔字符数
# l = 每周所占的行数
# c = 每个月之间的间隔字符数
cal = calendar.calendar(2019)
print(type(cal))
print(cal)

cal = calendar.calendar(2019, l = 0, c = 5)

# isleap: 判断某一年是否是闰年
print(calendar.isleap(2019))

# leapdays: 获取指定年份之间闰年的个数
print(calendar.leapdays(1998,2019))

# month(）：获取某个月的日历字符串
# 格式：calendar,month(年，月)
# 回值：月日历的字符串
print(calendar.month(2019, 5))

# monthrange()： 获取一个月的周几开始即和天数
# 格式calendar.monthrange(年，月)
# 回值：元组(周几开始, 总天数)
# 注意: 周默认0 - 6表示周一到周日

w = calendar.monthrange(2019, 5)
print(w)

w,t = calendar.monthrange(2019, 5)
print(w)
print(t)

# monthcalendar(): 返回一个月每天的矩阵列表
# 格式：calendar.monthcalender(年, 月)
# 回值：二级列表
# 注意：矩阵中没有天数用0表示
m = calendar.monthcalendar(2019,5)
print(m)

# prcal: 直接打印日历
calendar.prcal(2019)

# prmonth() 直接打印整个月的日历
# 格式：calendar.prmonth(年, 月)
# 返回值： 无
print(calendar.prmonth(2019, 5))

# weekday()获取周几
# 格式：calendar.weekday(年, 月, 日)
# 返回值：周几对应的数字
print(calendar.weekday(2019, 5, 2))

# 时间模块的属性
# timezone:当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔,东八区的是 -28800
# altzone: 获取当前时区于UTC时间相差的秒数，在没有夏令时的情况下
print(time.timezone)
# daylight: 测当前是否是夏令时的状态
print(time.daylight)
# 得到时间戳
print(time.time())
# time.localtime() : 返回当前时间
# 可以通过点号操作符得到相应的属性元素的内容
print(time.localtime())
t = time.localtime()
print(t.tm_hour)

# asctime() 返回元组的正常字符串化之后的时间模式
# 格式：time.asctime(时间元组)
# 返回值：字符串 Tue Jun 6 21:07:00 2019
t = time.localtime()
tt = time.asctime(t)
print(tt)

# ctimel: 获取字符串化的当前时间
t = time.ctime()
print(type(t))
print(t)

# mktime() ：使用时间元组获取对应的时间戳
# 格式：time.mktime(时间元组)
# 返回值： 浮点数时间戳

lt = time.localtime()
ts = time.mktime(lt)
print(type(ts))
print(ts)

# clock: 获取cpu时间，3.0-3版本直接使用，3.6调用有问题

# sleep: 睡眠
# 把时间表示成， 2019年5月2日  22:33
t = time.localtime()
ft = time.strftime("%Y年%m月%d日 %H:%M" , t)
print(ft)

# datetime常见属性
# datetime,date:一个理想和的日期，提供year，month, day属性
dt = datetime.date(2019, 5, 2)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)

# datetime.datetime :提供日期和时间的组合
# datetime.timedelta: 提供一个时间差，时间长度
# 常用类方法：
# today:
# now:
# utcnow
# fromtimestamo:从时间戳中返回本地时间
dt = datetime(2019,5,2)
print(dt.today())
print(dt.now())

print(dt.fromtimestamp(time.time()))
# datetime.timedelta : 表示一个时间间隔

t1 = datetime.now()
print(t1)
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
# td表示以小时的时间长度
td = timedelta(hours=1)
# 当前时间加上时间间隔后，把得到的一个小时后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))

# timeit-时间测量工具

# 测量程序运行时间间隔实验
def p():
    time.sleep(3.6)

t1 = time.time()
p()
print(time.time() - t1)

# 生成列表两种方法的比较
# 如果单纯比较生成一个列表的时间，可能很难实现
c = ''''''
sum = []
for i in range(1000):
    sum.append(i)
''''''
# 利用timeit调用代码，执行100000次，查看运行时间
t = timeit.timeit(stmt = "[i for i in range(1000)]", number=100000)
# 测量代码c执行100000次运行结果
t1 = timeit.timeit(stmt = c, number=100000)
print(t)
print(t1)

# timeit :可以执行一个函数，来测量一个函数的执行时间(下面代码报错)
def doIt():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))
# 执行函数重复10次
t = timeit.timeit(stmt = doIt(), number=10)
print(t)
'''
s = '''
def doIt(num):
    for i in range(num):
        print("Repeat for {0}".format(i))

# 执行doIt(num)
# setup负责把环境变量准备好
# 实际上相当于给timeit创造了一个小环境
# 再创作的小环境中代码执行的顺序是:
''''''
def doIt(num):
    .....
num = 3
doIt(num)
''''''
t = timeit.timeit("doIt(num)", setup=s+"num=3", number=10)


# getcwd() 获取当前工作目录
# 格式： os.getcwd()
# 返回值：当前工作目录的字符串

mydir = os.getcwd()
print(mydir)

# chdir() 改变当前的工作目录
# change directory
# 格式：os.chdir(路径)
# 返回值：无

os.chdir("D:/learn/python/tuling")
mydir = os.getcwd()
print(mydir)

# listdir()获取一个目录中所有子目录和文件的名称列表
# 格式：os.listdir(路径)
# 返回值：所有子目录和文件名称的列表

lis = os.listdir("D:/learn/python/tuling")
print(lis)

# makedirs()递归创建文件夹
# 格式：os.makedirs(递归路径)
# 返回值：无
# 递归路径：多个文件夹层层包含的路径就是递归的路径，例如 a/b/c

rst = os.makedirs("rui")
print(rst)

# system()运行shell命令
# 格式：os.system(系统命令)
# 返回值：打开一个shell或者终端界面
# 一般使用subprocess代替

# ls是列出当前文件和文件夹的系统命令
# rst = os.system("ls")
# print(rst)
# 在当前目录下创建一个rui,haha 的文件集
rst = os.system("touch rui.haha")
print(rst)

# getenv() 获取指定的系统环境变量值
# 相应的还有putenv
# 格式：os.getenv("环境变量名")
# 返回值：指定环境变量名对应的值
rst = os.getenv("path")
print(rst)

# exit() 退出当前程序
# 格式：exit()
# 返回值：无

print(os.pardir)
print(os.curdir)
print(os.sep)
print(os.name)

# abspath() 将路径转换为绝对路径
# 格式：os.path.abspath(”路径“)
# 返回值: 路径的绝对路径形式

# linux中
# . 号代表当前目录
# .. 代表父目录
absp = op.abspath(".")
print(absp)

# basename() 获取路径中的中文名部分
# 格式：os.parh.basename("路径")
# 返回值：文件名字符串

bn = op.basename("D:/learn/python")
print(bn)
bn = op.basename("D:/learn/python/tuling")
print(bn)

# join() 将多个路径拼合成一个路径
# 格式： os.path.join(路径1， 路径2......)
# 返回值： 组合之后的新路径字符串
bd = "D:/learn/python/tuling"
fn = "rui"
p = op.join(bd, fn)
print(p)

# split() 将路径切割为文件夹部分和当前文件部分
# 格式：os.path.split(路径)
# 返回值：路径和文件名组成的元组

t = op.split("D:/learn/python/tuling/2")
print(t)

d,p = op.split("D:/learn/python/tuling/2")
print(d,p)

# isdir() 检测是否是目录
# 格式： os.path.isdir(路径)
# 返回值：布尔值
rst = os.path.isdir("D:/learn/python/tuling/2")
print(rst)
rst = os.path.isdir("D:/learn/python/tuling")
print(rst)

# exists()检测文件或目录是否存在
# 格式：os.path.exists(路径)
# 返回值：布尔值

e = op.exists("D:/learn/python")
print(e)
e = op.exists("D:/learn/python/tuling/2.py")
print(e)
e = op.exists("D:/learn/pyhon")
print(e)

# shutil 模块
# copy() 复制文件
# 格式：shutil.copy(来源路径, 目标路径)
# 返回值：返回目标路径
# 拷贝的同时，可以给文件重命名

rst = shutil.copy("D:/learn/python/tuling/2.py", "D:/learn/python/2copy.py")
print(rst)

# copy2() 复制文件，保留元数据(文件信息)
# 格式：shutil.copy2(来源路径, 目标路径)
# 返回值：返回目标路径
# copy2和copy的区别在于copy2复制文件时尽量保留元数据

# copyfile() 将一个文件中的内容复制到另一个文件当中
# 格式：shutil.copyfile("来源路径", "目标路径")
# 返回值：目标路径

cf = shutil.copyfile("D:/learn/python/tuling/a.txt", "D:/learn/python/tuling/b.txt")
print(cf)

# move() 移动文件/文件夹
# 格式：shutil.move("来源路径", "目标路径")
# 返回值：目标路径

# make_archive() 归档操作
# 格式：shutil.make_archive(”归档之后的目录和文件名“， ”后缀“, "需要归档的文件夹“)
# 返回值： 归档后的地址
import shutil
# 是想得到一个后缀名为me的文件
rst = shutil.make_archive("D:/learn/python/tuling/rui_archive", "zip", "D:/learn/python/tuling/rui")
print(rst)

# unpack_archive()解包操作
# 格式：shutil.unpack_archive(”归档文件地址“, "解包后的地址“)
# 返回值：解包之后的地址

# zipfile
# zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
# 创建一个ZipFile对象，表示一个zip文件，参数file表示文件的路径或类文件对象
zf = zipfile.ZipFile("D:/learn/python/TU/a.zip")
# ZipFile.getinfo(name):
# 获取zip文件类指定的文件信息，返回一个zipfile.ZipInfo对象，它包括文件的详细信息

# rst = zf.getinfo("D:/learn/python/TU/a.zip")

# ZipFile.name.list()
# 获取zip文件类锁头文件的名称列表
nl = zf.namelist("D:/learn/python/TU/")
print(nl)

zf = zipfile.ZipFile("D:/learn/python/TU/a.zip")
# ZipFile.extractall([path[, members[, pwd]]])
# 解压zip包中所有文件到当前目录
rst = zf.extractall("D:\learn\python\TU")

# random() 获取0-1之间的随机小数
# 格式：randmo.random()
# 返回值：随机0-1之间的小数

print(random.random())

# 利用random函数，生成0-100直接整数

# choice() 随机返回序列中的某个值
# 格式：random.choice(序列)
# 返回值：序列中的某个值
l = [str(i) +"haha" for i in range(10)]
print(l)
rst = (random.choice(l))
print(rst)

# shuffle()随机打乱列表
# 格式：random.shuffle(列表)
# 返回值：打乱顺序之后的列表

l1 = [i for i in range(10)]
print(l1)

random.shuffle(l1)
print(l1)
'''
# randint(a, b): 返回一个a到b之间的随机整数，包含a和b
print(random.randint(0,100))