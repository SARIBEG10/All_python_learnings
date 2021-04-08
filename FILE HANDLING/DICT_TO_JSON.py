import json, os
"""WRITE DICT TO JSON FILES"""
dictionary = {"name": "saribeg", "age": 27, "company": "saralmas"}
a = []
for i in range(10):
    a.append(i)
with open("dict.json", "+r") as d:
    # os.remove("dict.json")
    # js = json.dumps(dictionary)
    # d.write(js)
    loader = json.load(d)
    print(loader)
