"""RAISE OWN EXCEPTION"""

# ID = int(input("Enter your ID: "))
# if ID < 0:
#     raise ValueError("you must enter positive values")
# else:
#     print("your ID is {}".format(ID))

try:
    ID = int(input("Enter your ID: "))
    if ID < 0:
        raise ValueError
except ValueError:
    print("you must enter positive values")
else:
    print("your ID is {}".format(ID))
finally:
    print("Goodbye dear user")