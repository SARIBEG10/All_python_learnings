import pickle

dictionary = {"name": "saribeg", "age": 27, "company": "saralmas", "salary": 5000, "University": "Azad"}

with open("dict.pkl", "+rb") as d:
    # pkl = pickle.dumps(dictionary)
    # d.write(pkl)
    pkld = pickle.load(d)
    print(pkld)
