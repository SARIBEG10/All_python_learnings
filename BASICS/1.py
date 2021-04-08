
a = 1
while a < 4:
    print('saribeg')
    a += 1
    if a == 3:
        print(a)
        break


# b = 40
# if b > 30:
#     print("the result is greater than 30")
# elif b < 30:
#     print("the result is lower than 30")
# else:
#     print("equality")
#
#

# Name = input(" Enter your name, please: ").capitalize()
# Name = input(" Enter your name, please: ").casefold()
# print("Hell {}".format(Name))


Name = "saribeg farmanian"
print("Hello {}".format(Name))
print(Name.encode())
print(Name.count('r'))
print(Name.endswith('g'))
print(Name.find('a'))
print(Name.isalpha())
# y = Name.join("-")
# y = Name.partition('s')
y = Name.partition(Name)
y = Name.replace('saribeg', 'Seda')
y = Name.rfind('a')
y = Name.title()
y = Name.capitalize()
y = Name.upper()
y = Name.zfill(22)
print(y)
Name = "12345"
print(Name.isalnum())

# print(type(a))
# a = 2.2
# print(type(a))
#

# b = 5
# d = complex(a, b)
# x = "sari"
# y = 'farmanian'
#
# print(d)

# print(y[3])


"""SET OPERATORS"""

x = {1, 2, 3}
y = {3, 4, 5, 6}

uni = x.union(y)
print(uni)

intersection = x.intersection(y)
print(intersection)

diff = x - y
print(diff)

symdiff = x.symmetric_difference(y)
print(symdiff)

x = {5, 8, 9}
y = {5, 6, 7, 8, 9}
subset = x.issubset(y)
superset = y.issuperset(x)
print(subset)
print(superset)


fruits = {('mango', 'apple'), 'guava', 'guava'}
# fruits.add(('mango', 'apple'))
# fruits.remove('guava')
print(fruits)


dictionary = {'name': 'Saribeg', 'age': 27}
fr = frozenset(dictionary)
print(dictionary)
print(fr)
print('-' * 40)
print('ARITHMETIC OPERATORS')
"""ARITHMETIC OPERATORS"""

x = 4
y = 5
x += y
print(x)
print(y)
print(x * y)
print(x - y)
print(x + y)
print(x / y)
print(x // y)
print(x % y)


"""BINARY OPERATORS """

x = 5
y = 3

bin_and = x & y
print(bin_and)

bin_or = x | y
print(bin_or)

right_shift = x >> 2
print(right_shift)

left_shift = x << 2
print(left_shift)


"""IDENTITY OPERATORS"""

x = 'hello'
y = 'hello'

x = 'hello'
y = 2
print(x is y)
print(x is not y)


a = [1, 2, 3, 4, 5]

print(1 in a)
print(1 not in a)
print('=' * 40)

"""BOOLEAN VARIABLES"""

x = False
y = None
z = True
print(bool(x))
print(bool(y))
print(bool(z))

a = 4
b = 5
print(bool(a == b))
print(bool(a < b))
print(bool())


one = 1
zero = 0
print(bool(one))
print(bool(zero))

# a = input("Please enter your num : ")


def is_even(num):
    return bool(num % 2 == 0)


if is_even(20):
    print("EVEN")
else:
    print("ODD")

print('=' * 40)

""" COMPARISON AND LOGICAL OPERATORS"""

a = 4
b = 4
print(a == b)
print(a != b)
print(5 == 6)
print(5 <= 6)


x = 3
y = 5
# y ^= x
# print(y)

print(x & y)
print(x | y)
print(x ^ y)