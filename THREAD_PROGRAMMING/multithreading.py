from threading import Thread
import threading
from time import sleep


def naturalNo():
    print(threading.current_thread().getName(), "Has Started")
    sleep(2)
    for c in range(10):
        print(c)

    print(threading.current_thread().getName(), "Has Ended")


if __name__ == "__main__":

    t1 = Thread(target=naturalNo)
    t2 = Thread(target=naturalNo)
    t1.start()
    t2.start()


