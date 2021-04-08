import re

pattern = "Saribeg has Covid-19"

x = re.compile(pattern)

y = x.match("Saribeg has Covid-19")

if y:
    print("Match found")
else:
    print("Match not found")
