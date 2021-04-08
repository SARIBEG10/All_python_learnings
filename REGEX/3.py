import re


pattern = "Hello"
s = re.search(pattern, "Hello world")

if s:
    print("Match is found")
else:
    print("Match not found")