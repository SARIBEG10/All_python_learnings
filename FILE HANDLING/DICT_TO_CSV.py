import csv
"""WRITE DICTIONARY TO CSV FILE"""
dictionary = {"name": "saribeg", "age": 27, "company": "saralmas"}

writer = csv.writer(open("dict.csv", "w"))
for key, val in dictionary.items():
    writer.writerow([key, val])

reader = csv.reader(open('dict.csv', 'r'))
for row in reader:
    print(row)