
##通过thread 实现django中
import threading
import time


class PrintThread(threading.Thread):
    def run(self):
        print("start.... %s" % (self.getName(),))
        for i in range(5):
            time.sleep(1)
            print("start.... %s" % (self.getName(),))

if __name__ == '__main__':
    prints = PrintThread()
    prints.start()
    print("开始了吗")