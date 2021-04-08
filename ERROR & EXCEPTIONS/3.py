"""ELSE BLOCK IN TRY """

try:
    ID = int(input("Enter your ID: "))
except ValueError:
    print("It wasn't integer")
else:
    print("your ID is {}".format(ID))
finally:
    print("It's end of your block")










