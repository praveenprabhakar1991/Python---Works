# WAP for Diamond Pattern for Numbers

col = 5
row = 1

for i in range(col-1):
    for j in range(i,col):
        print(' ', end = ' ')
    for j in range(i+1):
        print(row, end = ' ')
    for j in range(i):
        print(row, end = ' ')
    print()

for i in range(col):
    for j in range(i+1):
        print(' ', end = ' ')
    for j in range(i,col):
        print(row, end = ' ')
    for j in range(i,col-1):
        print(row, end = ' ')
    print()

print('\n*** You Can Try ***\n')

user = int(input('Enter any Number : '))
print()

for i in range(user-1):
    for j in range(i,user):
        print(' ', end = ' ')
    for j in range(i+1):
        print(user, end = ' ')
    for j in range(i):
        print(user, end = ' ')
    print()
    
for i in range(user):
    for j in range(i+1):
        print(' ', end = ' ')
    for j in range(i,user):
        print(user, end = ' ')
    for j in range(i, user-1):
        print(user, end = ' ')
    print()
    