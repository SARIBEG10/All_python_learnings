class Comparison(object):

    def __init__(self, x):
        self.x = x

    def __gt__(self, other):
        return self.x > other.x

    def __lt__(self, other):
        return self.x < other.x

    def __eq__(self, other):
        return self.x == other.x

    def __le__(self, other):
        return self.x <= other.x

    def __ge__(self, other):
        return self.x >= other.x


if __name__ == "__main__":

    obj1 = Comparison(2)
    obj2 = Comparison(3)
    print(obj2 > obj1)
    print(obj1 <= obj2)
    print(obj1 >= obj2)






