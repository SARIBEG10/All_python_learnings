from threading import Thread
import threading


def enev_odd():
    even_No()
    odd_No()
    print(threading.currentThread().getName())


def even_No():
    print("Even No are \n")
    for i in range(0, 5):
        if i % 2 is 0:
            print(i)
    print(threading.currentThread().getName())


def odd_No():
    print("Odd No are \n")
    for x in range(0, 5):
        if x % 2 is not 0:
            print(x)
    print(threading.currentThread().getName())


my_thread = Thread(target=enev_odd, name="Even and Odd thread")
my_thread.start()
