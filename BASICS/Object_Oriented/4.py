class Parent:
    """
        This OOP example for Inheritance and Inheritance Types
    """
    def __init__(self):
        print("This is parent")

    def parent_method(self):
        print("first parent method")

    def parentmethodnext(self):
        print("This is the next overwrited method in Parent class")


class Child(Parent):

    def __init__(self):
        print("This is Child class")

    def child_method(self):
        print("This is child class first method")

    def parentmethodnext(self):     # method Overwriting
        print("for child class")


class moreChilds(Child):
    """
        This is Multi-Level Inheritance when you inherit from Child class
        of another class.
    """

    def __init__(self):
        print('more childs')

    def child_method(self):
        print('more childs method')


class CHild2(Parent):
    """
        This is multiple Inheritance example
    """
    def __init__(self):
        print('Child2 class')

    def Child_2_method(self):
        print("I'm the second child of Family ")


class Multiple(Child, CHild2):
    """
        Hybrid Inheritance
    """

    def __init__(self):
        print('Multiple Class')

    def multiplemethod(self):
        print('multiplemethod')


if __name__ == "__main__":

        p = Parent()
        c = Child()
        c2 = CHild2()
        mo = moreChilds()
        m = Multiple()

        m.child_method()
        m.parent_method()