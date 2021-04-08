import math
a = 2
b = 3
c = a + b
print(c)

x = 'Sari '
y = ' Farmanian'
z = x + y
print(z)


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * 2

    def getradius(self):
        return self.radius

    def __add__(self, other_radius):
        return Circle(self.radius + other_radius.radius)


if __name__ == "__main__":

    c1 = Circle(6)
    c2 = Circle(5)
    c3 = c1 + c2
    print(c3.getradius())
    



