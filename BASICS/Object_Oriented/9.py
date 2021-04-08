"""ABSTRACT CLASS & ABSTRACT METHOD"""

from abc import ABC, abstractmethod


class Mathoperations(ABC):

    @abstractmethod
    def sume(self, a, b):
        pass

    @abstractmethod
    def division(self, a, b):
        pass

    @abstractmethod
    def multiply(self, a, b):
        pass


class Calculator(Mathoperations):

    def sume(self, a, b):
        print(a+b)

    def division(self, a, b):
        print(a/b)

    def multiply(self, a, b):
        print(a*b)


if __name__ == "__main__":

    a = Calculator()
    a.sume(1, 2)
