import copy
"""COPY MODELS IN PYTHON"""
# Normal copy

list11 = [1, 2, 3, 4, 5, 6]
list2 = list11

list2[2] = 20


print(list11)
print(list2)


print(id(list11))
print(id(list2))


# Shallow copy

old_list = [[1, 2, 3], 4, 5, 6]

new_list = copy.copy(old_list)

new_list[0][1] = 9
print(new_list)
print(old_list)

print(id(new_list))
print(id(old_list))


# Deep copy

my_list = [1, 2, 3, 4, 5]

my_list1 = copy.deepcopy(my_list)

my_list1[1] = 30
print(my_list)
print(my_list1)

print(id(my_list))
print(id(my_list1))