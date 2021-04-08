import re

pattern = "Salmasi"

x = re.subn(pattern, 'Haftevani', 'Saribeg Farmanian Salmasi, Salmasi', count=0)
print(x)
