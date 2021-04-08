"""POLYMORPHISM EXAMPLE"""


class Cat:

    def sound(self):
        print("Meow meow!")

    def swim(self):
        print("Cats  can't swim")

    def color(self):
        print("Cats are in different colors")


class Duck:

    def sound(self):
        print("Quack quack!")

    def swim(self):
        print("Ducks can swim")

    def color(self):
        print("Usually black & White")


def animaltype(animal):
    animal.sound()
    animal.swim()
    animal.color()


if __name__ == "__main__":
    Garfield = Cat()
    Duffy = Duck()

    animaltype(Garfield)
    animaltype(Duffy)



