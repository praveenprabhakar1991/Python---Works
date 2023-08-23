# WAP for (.) and (..) - period regular Expression
# . period finds single letter in a given string
# .. period finds double letters in a given string

import re

str = 'abcdefghijklmnopqrstuvwxyz'                   # regex does not read ['List'] or {'Dict'}

# regex = re.search(r'..', str)                      # re.search finds the match and show the index of the string only One time
# regex = re.match(r'..', str)                       # re.match finds the match and show the index of the string only one time
regex = re.finditer(r'..', str )                     # re.finditer finds the match and show the index of the string by using for loop
for reg in regex:
    print(reg)
    
regex1 = re.findall(r'.', str)                       # re.findall finds the match and converts the strings into lists
print(regex1)

regex2 = re.findall(r'..', str)                      
print(regex2)