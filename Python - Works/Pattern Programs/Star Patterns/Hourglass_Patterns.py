# WAP for Hour Glass Pattern

n = 5

for i in range(n):
    for j in range(i+1):
        print(' ', end = ' ')
    for j in range(i,n):
        print('*', end = ' ')
    for j in range(i,n-1):
        print('*', end = ' ')
    print()
    
for i in range(n):
    for j in range(i,n):
        print(' ', end = ' ')
    for j in range(i):
        print('*', end = ' ')
    for j in range(i+1):
        print('*', end = ' ')
    print()
    
print('\n*** You Can Try ***\n')

user = int(input('Enter any Number : '))
print()

for i in range(user):
    for j in range(i+1):
        print(' ', end = ' ')
    for j in range(i,user):
        print('*', end = ' ')
    for j in range(i,user-1):
        print('*', end = ' ')
    print()

for i in range(user-1):
    for j in range(i,user):
        print(' ', end = ' ')
    for j in range(i):
        print('*', end = ' ')
    for j in range(i+1):
        print('*', end = ' ')
    print()
