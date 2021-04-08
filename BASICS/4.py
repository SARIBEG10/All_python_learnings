import functools
"""FUNCTIONS"""


def square(x, y):
    print(abs(x), abs(y))


square(-3, -9)


def addition():
    a = 4
    b = 6
    return print(a + b)


def multiplication():
    a = 4
    b = 6
    print(a * b)


multiplication()
addition()


def Education(status):

    if status == 'I':
        status = "Qualified"
        print(status)
    else:
        print("Unqualified")


Education("r")


def selfie(name="saribeg", age=27, job="backend developer"):
    print(name, age, job)


selfie()


selfie(name='Umair', age=23, job='IT manager')

""""UNPACKING ARGUMENTS"""


def selfie(name, age, job):
    print(name, age, job)


data = ("saribeg", 27, "backDev")
selfie(*("saribeg", 27, "backDev"))
selfie(*data)
selfie(data[0], data[1], data[2])


"""REDUCING FUNCTIONS"""

my_list = []
for i in range(10):
    my_list.append(i)

print(functools.reduce(lambda a, b: a+b, my_list))

print(functools.reduce(lambda a, b: a > b, my_list))
"""PARTIAL FUNCTIONS"""


def my_func(a, b, c, d):
    return a+b+c+d


par = functools.partial(my_func, 3, 4, 5)
print(par(7))
print(par(8))