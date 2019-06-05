import threading
import time

# 参数定义最多几个线程同时使用资源
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        # 线程进来后循环打印，从6开始，
        for i in range(5):
            print(threading.currentThread().getName() + 'get semaphore')
        time.sleep(3)
        # 释放
        semaphore.release()
        # 打印释放者
        print(threading.currentThread().getName() + 'release semaphore')


for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()