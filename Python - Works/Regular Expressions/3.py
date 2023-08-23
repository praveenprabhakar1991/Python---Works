# WAP for ^ - Caret regular Expression
# ^ finds the opposite of the pattern in the string

import re

str = 'abcdefghijklmnopqrstuvwxyz'

regex = re.finditer(r'[^python]', str)
for reg in regex:
    print(reg)

regex1 = re.findall(r'[^python]', str)
print(regex1)