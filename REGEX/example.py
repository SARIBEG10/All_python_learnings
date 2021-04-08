import re


passwords = [
    "sari123",
    "hi235",
    "pass888",
    "ashot2535",
    "seda",
    "saribeg",
    "Ashot",
]

match_pattern = "[0-9]"

for x in passwords:
    r = re.search(match_pattern, x)
    if r:
        print(x + "Is valid password")
    else:
        print(x + "Is Invalid password")




