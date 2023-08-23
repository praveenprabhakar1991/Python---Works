# WAP for \d regular Expression
# \d finds only the digits in the string (0-9)
# \D finds (Alphabets) opposite of the digits in the string (a-z A-Z and symbols)

import re

str = '12 123 1234 12345 123456 1234567 12345678 123456789'

regex1 = re.finditer(r'\d{5,9}', str)
for reg in regex1:
    print(reg)
    
regex = re.findall(r'\d{5,9}', str)
print(regex)
print(len(regex))
