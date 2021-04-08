#
# my_dict = {'c': 1, 'a': 3, 'b': 2, 'd': 4}
# x = my_dict.keys()
# y = my_dict.items()
# z = my_dict.values()
# print(z)
# print(x)
# print(y)

# x = {k: v*2 for (k, v) in my_dict.items()}
# print(x)
#
# y = list(map(lambda v:  v*2, my_dict.values()))
# d = dict(zip(my_dict.keys(), y))
# print(d)


# di = {i: i**2 for i in range(20) if i % 2 == 0}
# for i in range(20):
#     if i % 2 == 0:
#         di[i] = i**2

# print(di)

# Nested dict comprehension

di = {'one': {'a': 1}, 'two': {'b': 2}}

for (external_key, external_value) in di.items():
    for (internal_key, internal_value) in external_value.items():
        external_value.update({internal_key: float(internal_value)})

print(di)
