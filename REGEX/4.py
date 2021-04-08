import re

x = re.split('\W', "Saribeg,Farmanian")
print(x)

pattern = 'Saribeg'
y = re.findall(pattern, 'Saribeg is very strong')
print(y)