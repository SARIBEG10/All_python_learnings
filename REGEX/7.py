import re
import string

pattern = '\!@#$%^&*~'
x = re.escape(pattern)
# print(x)

pattern = string.ascii_letters
y = re.escape(pattern)
print(y)

p = string.hexdigits
print(re.escape(p))
