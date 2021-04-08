import re

pattern = 'Salmasi'
x = re.sub(pattern, 'Haftevani', 'Saribeg Farmanian Salmasi', count=0)
print(x)
