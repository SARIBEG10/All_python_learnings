class Student:
    """
        This is example of method overloading
    """
    def __init__(self, name="Ilan", age=35, University='MIT'):
        self.name = name
        self.age = age
        self.University = University
        print(self.University, self.name, self.age)


class Student2(Student):

    def __init__(self):
        super().__init__(name='Saribeg', age=27)


if __name__ == "__main__":

    Ilan = Student()
    Sari = Student2()
    Ali = Student(name='Ali')