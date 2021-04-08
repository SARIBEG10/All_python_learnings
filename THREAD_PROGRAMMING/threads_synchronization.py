from threading import Thread
import threading


class Reservation(object):

    # l = threading.Semaphore()
    l = threading.Lock()

    def __init__(self, ticket_left):
        self.ticket_left = ticket_left

    l.acquire()

    def reservation(self, reservedticket):
        if self.ticket_left >= reservedticket:
            print("your reservation is confirmed")
            print("pls make a payment")
            self.ticket_left -= reservedticket

        else:
            print("there is not enough ticket")
    l.release()


if __name__ == "__main__":
    obj1 = Reservation(9)
    t1 = Thread(target=obj1.reservation, args=[3])
    t2 = Thread(target=obj1.reservation, args=[4])
    t3 = Thread(target=obj1.reservation, args=[3])
    t1.start()
    t2.start()
    t3.start()
