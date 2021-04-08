import random

random.seed(12)  # plant this seed in the place of the memory therefore when we run
# program each time the output result is the same for the random module and its methods
b = random.random()
print(b)
y = random.randint(2, 6)
print(y)

z = random.randrange(10, 50, 5)
print(z)


