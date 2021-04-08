class Addition(object):

    def __init__(self, *arguments):
        if len(arguments) == 0:
            self.numbers = (0, 0)
        else:
            self.numbers = arguments

    def __add__(self, other):
        sum = tuple(x + y for x, y in zip(self.numbers, other.numbers))
        return Addition(*sum)

    def __sub__(self, other):
        sub = tuple(x - y for x, y in zip(self.numbers, other.numbers))
        return Addition(*sub)

    def __mul__(self, other):
        mul = tuple(x * y for x, y in zip(self.numbers, other.numbers))
        return Addition(*mul)


if __name__ == "__main__":

    obj1 = Addition(2, 3)
    obj2 = Addition(4, 5)
    obj3 = obj1 + obj2
    obj4 = obj1 - obj2
    obj5 = obj1 * obj2
    print(obj3.numbers)
    print(obj4.numbers)
    print(obj5.numbers)








