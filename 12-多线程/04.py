import time
import _thread as thread

def loop1(in1):
    print('Start loop 1 at:', time.ctime())
    print("我是参数", in1)
    time.sleep(4)
    print('End loop 1 at:', time.ctime())


def loop2(in1, in2):
    # ctime 得到当前时间
    print('Start loop 2 at:', time.ctime())
    print("我是参数", in1, "和参数", in2)
    time.sleep(2)
    print('End loop 2 at:', time.ctime())


def main():
    print("Start loop 2 at:", time.ctime())