class Unary(object):

    def __init__(self, x):
        self.x = x

    def __neg__(self):
        x = -self.x
        return "The negative is " + str(x)

    def __pos__(self):
        x = self.x
        return "The positive is " + str(x)

    def __repr__(self):
        return "The Unary return for No : " + str(self.x)


if __name__ == "__main__":

    obj1 = Unary(3)
    print(-obj1)
    print(+obj1)
    print(repr(obj1))





