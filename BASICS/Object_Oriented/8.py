"""COMPOSITION  & AGGREGATION"""


class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("weeee, its fun i can fly")
        elif self.ratio == 1:
            print("Its hard but I try to fly")
        else:
            print("I can't fly")


class Color(object):
    """
        This is the Aggregation example class
    """

    def __init__(self, color):
        self.color = color

    def rang(self):
        print(self.color)


class Duck(object):

    def __init__(self, color):
        self._wing = Wing(1.8)
        self.color = color

    def walk(self):
        print("chalap chulup")

    def swim(self):
        print("weeeeeeeeeee, its chill")

    def quack(self):
        print("Quack quack quack")

    def fly(self):
        self._wing.fly()

    def rang(self):
        self.color.rang()


class Penguin(object):

    def walk(self):
        print("latii rah mire")

    def swim(self):
        print("goshadi shena mikone")

    def quack(self):
        print("No quack")


def animal(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == "__main__":

    Ghermez = Color('Abi')      # aggregation example

    Duffy = Duck(Ghermez)

    larvin = Penguin()

    Duffy.fly()

    Duffy.rang()

    animal(Duffy)
    print('=' * 40)
    animal(larvin)
