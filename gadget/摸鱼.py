import time
from threading import Thread, Lock

# 摸鱼


def moyu_time(name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s 开始摸鱼 %s" % (name, time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1

class MyThread(Thread):
    def __init__(self, threadID, name, counter):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程：" + self.name)
        moyu_time(self.name, self.counter, 10)
        print("退出线程：" + self.name)

thread1 = MyThread(1, "小明", 1)
thread2 = MyThread(2, "小红", 1)

# 开启新线程
thread1.start()
thread2.start()
# 等待至线程中止
thread1.join()
thread2.join()
print ("线程===end")

# 单线程
# moyu_time('小帅b', 1, 20)