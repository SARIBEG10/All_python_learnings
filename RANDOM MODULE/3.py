import random

l1 = ['banana', 'apple', 'coconut', 'cherry']
l2 = [1, 2, 3, 4, 5, 6, 7]
x = random.sample(l1, 2)
print(x)

y = random.choices(l2, k=2)
print(y)

z = random.choice(l2)
print(z)