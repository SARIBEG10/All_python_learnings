class EAO(object):

    def __init__(self, x):
        self.x = x

    def __iadd__(self, other):
        x = self.x + other.x
        return x

    def __imul__(self, other):
        x = self.x * other.x
        return x

    def __ifloordiv__(self, other):
        x = self.x // other.x
        return x


if __name__ == "__main__":
    obj1 = EAO(3)
    obj2 = EAO(4)
    # obj2 += obj1
    # print(obj2)
    # obj2 *= obj1
    # print(obj2)
    obj2 //= obj1
    print(obj2)








