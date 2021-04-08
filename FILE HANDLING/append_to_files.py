# path = "saribeg.csv"
# file = open(path, "a")
# file.write(" and i am 27 years old")
# file.close()

path = "sarinew.txt"
path1 = "saribeg.csv"

# file = open(path, "w+")
file = open(path1, "r")
data = file.read()
file.close()

file1 = open(path, "a")
file1.write(data)
file1.close()

