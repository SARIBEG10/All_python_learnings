from threading import Thread
import threading


class MyThread(Thread):
    def run(self):
        print("Egyptian Pyramid")
        print(threading.current_thread().getName())
        for i in range(0, 5):
            for j in range(0, i+1):
                print("*", end=" ")
            print("\r")


obj = MyThread()
obj.start()