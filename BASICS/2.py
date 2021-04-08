"""DICTIONARIES"""

fruits = {'banana': 'yellow', 'apple': 'red'}
print(fruits)
fruits['apple'] = 'orange'
print(fruits['apple'])

key1 = frozenset({1, 2, 3})
cities = {key1: 'Tehran', 2: 'Tabriz', (3, 4, 5): 'Isfahan', 4: 'Mashhad'}
# print(cities)
print(cities[key1])
cities[(5, 6, 7)] = 'Amol'
cities[5] = 'Shiraz'
cities[5] = 'Tabriz'
print(cities)
del cities[5]
print(cities)
print(cities.pop(2))
print(cities.keys())
print(cities.items())
print(cities.values())
print(cities.clear())
print(cities)
