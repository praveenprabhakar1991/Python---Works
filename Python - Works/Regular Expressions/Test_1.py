# WAP to convert the String into Dict Format using Regular Expression

import re

friends = ''' Praveen is 31 and Prabhakar is 33
            Gopi is 34 and partha is 33
            Deepu is 32 and Shravan is 33 
            kokila is 32 and Saakshi is 32
            James is 29 and kishore is 29 '''

names = re.findall(r'[A-Z][a-z]*', friends)
ages = re.findall(r'\d{2}', friends)

# print(names)
# print(ages)

# Converting to Dict format
dict_friends = {}
x = 0

for name in names:
    dict_friends[name] = ages[x]
    x += 1 # or x = x + 1
    
print(dict_friends)