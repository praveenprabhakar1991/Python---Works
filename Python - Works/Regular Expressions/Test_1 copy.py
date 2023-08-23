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

x = 0

for name in names:
    print(f'{name} : {ages[x]}')
    x += 1