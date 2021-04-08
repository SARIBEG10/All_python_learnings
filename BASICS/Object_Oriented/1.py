
class Saribeg:

    def sume(self):
        x = 4
        y = 5
        return x + y


class Seda(Saribeg):
    pass


a = Saribeg()
b = Seda()
print(a.sume())
print(b.sume())


class My_class():

    def name(self):
        print("This is a class method(function)")


def name():
    print("This is function")


name()

sari = My_class()
sari.name()

