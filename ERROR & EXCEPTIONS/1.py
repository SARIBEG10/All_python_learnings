""" SYNTAX ERROR - NAME ERROR"""


def hello():
    pint("hello")


try:
    hello()
except NameError:
    print("you catch Name error")

while True:
    try:
        age = int(input("Please enter your Age: "))
        if age < 19:
            print("you are teenager")
            break
        else:
            print("your age is {}".format(age))

    except ValueError:
        print("It's must be Int")
