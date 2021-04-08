import re

email = 'sari@gmail.com'
x = re.match('(.*)(@)(gmail)(.*)', email)
print(x.group())





