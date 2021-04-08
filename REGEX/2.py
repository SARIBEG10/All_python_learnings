import re

pattern = "saribeg is very strong"
x = re.match(pattern, 'saribeg is very strong')
if x:
    print("Match found")
else:
    print("Match not found")
