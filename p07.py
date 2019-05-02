import calendar
import time
import timeit
import datetime
from datetime import datetime, timedelta
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
'''
# 执行doIt(num)
# setup负责把环境变量准备好
# 实际上相当于给timeit创造了一个小环境
# 再创作的小环境中代码执行的顺序是:
'''
def doIt(num):
    .....
num = 3
doIt(num)
'''
t = timeit.timeit("doIt(num)", setup=s+"num=3", number=10)