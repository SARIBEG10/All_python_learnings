"""EVERYTHING IS OBJECT"""
a = 2
b = 2.2
c ="Saribeg"

print(type(a))
print(type(b))
print(type(c))


class Iitializer_Example():

    def __init__(self, object):
            print(object)


d = Iitializer_Example("Salam Donya")


class Calculator:
    """This class is intended for calculation"""

    def __init__(self, a, b):
        print(a + b)
        print(a - b)
        print(a * b)
        print(a / b)


cl = Calculator(1, 2)

help(Calculator)
print(Calculator.__doc__)
