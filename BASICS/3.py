"""OPERATORS PRECEDENCE"""
a = 1 + 7 * 2 ** 2 / 2 // 2
print(a)

""" LIST AND TUPLES"""

l1 = [1, "salam", [1, 2, 3], "salam"]
print(l1)

print('=' * 40)
l1[2] = 2
print(l1.pop(1))
print(l1.remove(2))
l1.insert(0, 22)
l1.reverse()
print(l1)

t1 = ("apple", 1, "banana", 1)
print(t1)
print(t1[2])
print(t1[0])


dictionary1 = {2: 'apple', 5: 'banana', 3: 'grape', 1: 'cherry', 5: 'lemon'}
print(dictionary1)
