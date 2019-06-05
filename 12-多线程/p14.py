import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def func_1():
    print("func 1 starting...")
    lock1.acquire()
    print("func 1 申请了 lock1...")
    time.sleep(2)
    print("func 1 等待 lock2...")
    lock2.acquire()
    print("func 1 申请了 lock2...")

    lock2.release()
    print("func 1 释放了 lock2...")

    lock1.release()
    print("func 1 释放了 lock1...")

    print("func 1 done.....")


def func_2():
    print("func 2 starting...")
    lock2.acquire()
    print("func 2 申请了 lock2...")
    time.sleep(2)
    print("func 2 等待 lock1...")
    lock1.acquire()
    print("func 2 申请了 lock1...")

    lock1.release()
    print("func 2 释放了 lock1...")

    lock1.release()
    print("func 2 释放了 lock2...")

    print("func 2 done.....")

if __name__ == '__main__':

    print("主程序启动......")
    t1 = threading.Thread(target=func_1(),args=())
    t2 = threading.Thread(threading=func_2(),args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序启动......")












