from threading import Thread
import threading

# threading.currentThread().setName('mythread')
# t = threading.currentThread().getName()
# print(t)


def evenNumbers():
    for x in range(20):
        if x % 2 == 0:
            print(x)
    t = threading.currentThread().getName()
    print(t)


t = threading.currentThread().getName()
print(t)
my_thread = Thread(target=evenNumbers)
my_thread.start()





