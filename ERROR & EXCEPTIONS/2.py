"""MULTIPLE EXCEPTION"""
try:
    a = int(input("Please Insert your First Value: "))
    b = int(input("Please Insert your Second Value: "))
    print("The result is : {}".format(a/b))
except ValueError:
    print("Value Error... It must be an Integer")
except ZeroDivisionError:
    print("Zero Division Error... It can't divided by ZERO")
