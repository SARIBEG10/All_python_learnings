from threading import Thread
import threading


class MyThread(object):

    def natural_numbers(self):
        if threading.current_thread().getName() == "Thread-1":
            for x in range(10):
                print(x)


if __name__ == "__main__":

    obj1 = MyThread()
    t = Thread(target=obj1.natural_numbers)
    t.start()

    a = threading.current_thread().getName()
    print(a)








