# WAP for \s regular Expression
# \s finds the empty space and new lines in the string (' ' , \n )
# \S finds (Alphanumeric) Opposite of empty space and new lines in the string (a-z A-Z and symbols)

import re

str = '''Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI)in the Netherlands as a successor
to the ABC programming language, which was inspired by SETL, capable of exception handling and interfacing with the Amoeba operating system.
Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, 
when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life", a title the Python community bestowed
upon him to reflect his long-term commitment as the project's chief decision-maker.In January 2019, active Python core developers elected a five-member 
Steering Council to lead the project.'''

# regex = re.finditer(r'\s', str)
# for reg in regex:
#     print(regex)
    
regex1 = re.findall(r'\s', str)
print(regex1)
print(len(regex1))
