# WAP to Rename/Replace the Word in a string using Regular Expression

import re

str = 'Welcome to Python. Python is a high-level Interpretor programming Language. Python is easy to learn'

print(str)

reg = re.compile('Python')
regex = reg.sub('JavaScript', str)

print(regex)
