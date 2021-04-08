import array
"""ARRAYS AND LISTS"""

# One Dimensional Array
l1 = [7, 8]
list1 = [1, 2, 3, 4, 5, 6]
list1.append([9, 10])
print(list1.extend(l1))

print(list1[0])
print(list1[1])

# Two Dimensional Array

list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list2[1][2])
print(list2[0][1])

arr1 = array.array('i', [1, 2, 3, 4])
# arr2 = array.array('b', ["saribeg", "seda", "ashot"])
arr1.insert(1, 1)
print(arr1)


print(list1 * 2)
print(list1)