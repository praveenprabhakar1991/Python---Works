col = 5

for i in range(col+1):
    stars = ' * ' * i
    space = '   ' * (2 *(col-i))
    print(stars + space + stars)
    
for j in range(col):
    stars = ' * ' * (col-j)
    space = '   ' * 2 * j 
    print(stars + space + stars)
    
print('\n*** You Can Try ***\n')

user = int(input('Enter any Number : '))
print()

for i in range(user+1):
    stars = ' * ' * i
    space = '   ' * (2 *(user-i))
    print(stars + space + stars)
    
for j in range(user):
    stars = ' * ' * (user-j)
    space = '   ' * 2 * j
    print(stars + space + stars)