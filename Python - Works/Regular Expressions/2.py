# WAP for [] - Square Bracket regular Expression
# [] finds the written pattern inside the sqaure bracket from the given string

import re

str = 'abcdefghijklmnopqrstuvwxyz'

regex = re.finditer(r'[python]', str )
for reg in regex:
    print(reg)
    
regex = re.findall(r'[python]', str)
print(regex)
print(len(regex))